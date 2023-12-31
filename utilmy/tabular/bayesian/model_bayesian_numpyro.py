"""Numpyro Bayesian regression.
Docs::

    import numpy as np
    import pandas as pd
    from numpyro import distributions as dist
    from utilmy.tabular.bayesian.model_bayesian_numpyro import Normal


    # random number generator seed, to reproduce exactly.
    RNG_KEY = np.array([0, 0])

    class Model(Normal):
        dv = "y"
        features = dict(
            const=dict(transformer=1, prior=dist.Normal(0, 1)),
            x=dict(transformer=lambda df: df.x, prior=dist.Normal(0, 1)),
        )


    df = pd.DataFrame(dict(x=[1, 2, 2, 3, 4, 5], y=[1, 2, 3, 4, 3, 5]))

    model = Model().fit(df, rng_key=RNG_KEY)
    # sample: 100%|██████████| 1500/1500 [00:04<00:00, 308.01it/s, 7 steps of size 4.17e-01. acc. prob=0.89]

    model.predict(df)



"""
import inspect
import json
import typing
from abc import ABC, abstractmethod
from functools import wraps
from random import randint

import numpy as onp
import numpyro
import pandas as pd
from jax import device_put
from jax import numpy as np
from jax import random
from jax.scipy.special import expit
from numpyro import diagnostics
from numpyro import distributions as dist
from numpyro import infer

#from . import exceptions



################################################################################################################
################################################################################################################
def test():
    import numpy as np
    import pandas as pd
    from numpyro import distributions as dist
    from utilmy.tabular.bayesian.model_bayesian_numpyro import Normal


    # random number generator seed, to reproduce exactly.
    RNG_KEY = np.array([0, 0])

    class Model(Normal):
        dv = "y"
        features = dict(
            const=dict(transformer=1, prior=dist.Normal(0, 1)),
            x=dict(transformer=lambda df: df.x, prior=dist.Normal(0, 1)),
        )


    df = pd.DataFrame(dict(x=[1, 2, 2, 3, 4, 5], y=[1, 2, 3, 4, 3, 5]))

    model = Model().fit(df, rng_key=RNG_KEY)
    # sample: 100%|██████████| 1500/1500 [00:04<00:00, 308.01it/s, 7 steps of size 4.17e-01. acc. prob=0.89]

    model.predict(df)

    """
    0    1.351874
    1    2.219510
    2    2.219510
    3    3.087146
    4    3.954782
    5    4.822418
    """

    model.predict(df, ci=True)

    """
              y  ci_lower  ci_upper
    0  1.351874  0.730992  1.946659
    1  2.219510  1.753340  2.654678
    2  2.219510  1.753340  2.654678
    3  3.087146  2.663617  3.526434
    4  3.954782  3.401837  4.548420
    5  4.822418  4.047847  5.578753
    """


    model.samples['x']
    """
    DeviceArray([[0.9443443 , 1.0215557 , 1.0401363 , 1.1768144 , 1.1752374 ,
    ...
    """

    model.samples_df.head()
    """
                    const         x
    chain sample                    
    0     0       0.074572  0.944344
          1       0.214246  1.021556
          2      -0.172168  1.040136
          3       0.440978  1.176814
          4       0.454463  1.175237
    """

    model.metrics(df)

    {'r': 0.8646920305474705,
    'rsq': 0.7476923076923075,
    'mae': 0.5661819464378061,
    'mape': 0.21729708806356265}
    #For per-point errors, use aggerrs=False. A pandas dataframe will be returned that you can join on your source data using its index.

    model.metrics(df, aggerrs=False)

    """
      residual         pe        ape
    0 -0.351874 -35.187366  35.187366
    1 -0.219510 -10.975488  10.975488
    2  0.780490  26.016341  26.016341
    3  0.912854  22.821353  22.821353
    4 -0.954782 -31.826066  31.826066
    5  0.177582   3.551638   3.551638
    """
    #You can use grouped_metrics to understand within-group errors. Under the hood, the predicted and actual dv are groupby-aggregated (default sum) and metrics are computed within each group.

    df["group"] = [1, 1, 1, 2, 2, 2]
    model.grouped_metrics(df, 'group')

    {'r': 1.0,
    'rsq': 1.0,
    'mae': 0.17238043177407247,
    'mape': 0.023077819594065668}
    model.grouped_metrics(df, "group", aggerrs=False)

    """
          residual        pe       ape
    group                              
    1     -0.209107 -3.485113  3.485113
    2     -0.135654 -1.130450  1.130450
    """
    #Saving and recovering a saved model
    #Shabadoo models have to_json and from_dict methods which allow models to be saved and recovered exactly.

    import json

    # export to a JSON string
    model_json = model.to_json()

    # recover the model
    model_recovered = Model.from_dict(json.loads(model_json))

    # check the predictions are the same
    model_recovered.predict(df).equals(model.predict(df))
    True


















################################################################################################################
################################################################################################################
class NumpyEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles numpy types."""

    def default(self, obj):
        """Encode numpy types or pass to default."""
        if isinstance(obj, (np.integer, onp.integer)):
            return int(obj)
        elif isinstance(obj, (np.floating, onp.floating)):
            return float(obj)
        elif isinstance(obj, (np.ndarray, onp.ndarray)):
            return onp.array(obj).tolist()
        else:
            return super(NumpyEncoder, self).default(obj)


def require_fitted(f):
    """Decorate a function to require the model to be fitted for usage."""

    @wraps(f)
    def wrapper(*args, **kwargs):
        if not args or not getattr(args[0], "fitted"):
            raise NotFittedError(f)
        return f(*args, **kwargs)

    return wrapper


def columns_with_null_data(df: pd.DataFrame) -> typing.List[str]:
    """Return a list of columns names that have any null data."""
    return pd.isnull(df).any(axis=0).loc[lambda x: x].index.values.tolist()


def metrics(y: pd.Series, yhat: pd.Series) -> typing.Dict[str, float]:
    """Return general fit metrics of one series against another."""
    res = dict()
    if y.shape[0] >= 2:
        res["r"] = onp.corrcoef(y, yhat)[0][1]
        res["rsq"] = res["r"] ** 2
    res["mae"] = onp.mean(onp.abs(y - yhat))
    res["mape"] = onp.mean(onp.abs(y - yhat) / y)
    return res


class BaseModel(ABC):
    """Abstract base class from which all model families inherit."""

    features: typing.Dict[str, typing.Dict[str, typing.Any]] = None
    dv = None

    # wrap the linear combination if inputs {lc} in newlines and the link function
    # for formula printing only
    _formula_link_str = "(\n{lc}\n)"

    # for when the model estimates nonfeature variables and we need to keep track.
    _additional_variables = []

    @staticmethod
    @abstractmethod
    def link(x):
        """Implement the link function for the model."""
        pass

    @abstractmethod
    def likelihood_func(self, yhat):
        """Return the likelihood distribution given predictions yhat."""
        pass

    def __init__(self, rng_seed: int = None):
        """Initialize the model object. Set some flags and runs some validations.
        
        Optionally set the rng seed.
        """
        if not self.features:
            raise IncompleteModel(self, "features")

        if not self.dv:
            raise IncompleteModel(self, "dv")

        for name, feature in self.features.items():
            for key in ("transformer", "prior"):
                if key not in feature:
                    raise IncompleteFeature(name, key)

        # this will be split each time randomness is needed.
        self.rand_key = random.PRNGKey(
            randint(0, 10000) if rng_seed is None else rng_seed
        )

        self.fitted = False

    def __repr__(self):
        """Print out the model name and the model family."""
        my_name = self.__class__.__name__
        mro = inspect.getmro(self.__class__)
        model_type = next(filter(lambda x: x[1] == BaseModel, zip(mro, mro[1:])), None)

        if model_type is None:
            return f"<Shabadoo Model: {my_name}>"

        model_type = model_type[0].__name__
        return f"<Shabadoo {model_type} Model: {my_name}>"

    def split_rand_key(self, n: int = 1) -> random.PRNGKey:
        """Split the random key, assign a new key and return the subkeys.
        
        Parameters
        ----------
        n : int
            Number of subkeys to generate. Default 1.
        Returns
        -------
        random.PRNGKey
            An array of PRNG keys or just a single key (if n=1).
        """
        keys = random.split(self.rand_key, n + 1)
        self.rand_key = keys[0]
        if n == 1:
            return keys[1]
        else:
            return keys[1:]

    @classmethod
    def transform(cls, df: pd.DataFrame) -> pd.DataFrame:
        """Transform a dataframe for model input.
        
        Parameters
        ----------
        df : pd.DataFrame
            Source dataframe to transform.
        Returns
        -------
        pd.DataFrame
            Dataframe containing transformed inputs.
        """
        return df.assign(
            **{
                feature_name: data["transformer"]
                for feature_name, data in cls.features.items()
            }
        )[cls.features.keys()]

    def model(self, df: pd.DataFrame):
        """Define and return samples from the model.
        
        Parameters
        ----------
        df : pd.DataFrame
            Input data for the model.
        """
        inputs = self.transform(df)
        coefs = np.array(
            [
                numpyro.sample(name, data["prior"])
                for name, data in self.features.items()
            ]
        )

        # apply link
        yhat = self.link(inputs.values @ coefs)

        # we should never see an unfitted model being run without the dv
        # as the dv should always be present for fitting
        if not self.fitted and self.dv not in df.columns:
            raise RuntimeError(
                "Trying to run an unfitted model without the dv present. "
                + "Something has gone wrong."
            )

        # if model is not fitted, this MUST be the call to .fit(), so add the obs.
        if not self.fitted:
            return numpyro.sample(
                self.dv, self.likelihood_func(yhat), obs=df[self.dv].values
            )

        # otherwise, this is a post-fit predict call or something, do not include an obs.
        return numpyro.sample(self.dv, self.likelihood_func(yhat))

    def fit(
        self,
        df: pd.DataFrame,
        sampler: str = "NUTS",
        rng_key: np.ndarray = None,
        sampler_kwargs: typing.Dict[str, typing.Any] = None,
        **mcmc_kwargs,
    ):
        """Fit the model to a DataFrame.
        
        Parameters
        ----------
        df : pd.DataFrame
            Source dataframe.
        sampler : str
            Numpyro sampler name. Default NUTS
        rng_key : two-element ndarray.
            Optional rng key, will be randomly splitted if not provided.
        sampler_kwargs :
            Passed to the numpyro sampler selected.
        **mcmc_kwargs :
            Passed to numpyro.infer.MCMC
        Returns
        -------
        Model
            The fitted model.
        """
        if self.fitted:
            raise AlreadyFittedError(self)

        if sampler.upper() not in ("NUTS", "HMC"):
            raise ValueError("Invalid sampler, try NUTS or HMC.")

        sampler = getattr(infer, sampler.upper())

        # store fit df
        self.df = df

        # check for nulls
        null_cols = columns_with_null_data(self.transform(df))
        if null_cols:
            raise NullDataFound(*null_cols)

        # set up mcmc
        _mcmc_kwargs = dict(num_warmup=500, num_samples=1000)
        _mcmc_kwargs.update(mcmc_kwargs)
        _sampler_kwargs = dict(model=self.model)
        _sampler_kwargs.update(sampler_kwargs or {})
        mcmc = infer.MCMC(sampler(**_sampler_kwargs), **_mcmc_kwargs)

        # do it
        rng_key_ = (
            self.split_rand_key() if rng_key is None else rng_key.astype("uint32")
        )
        mcmc.run(rng_key_, df=df)

        # store results
        self.samples = mcmc.get_samples(group_by_chain=True)
        self.fitted = True

        return self

    def predict(
        self,
        df: pd.DataFrame,
        ci: bool = False,
        ci_interval: float = 0.9,
        aggfunc: typing.Union[str, typing.Callable] = "mean",
    ) -> typing.Union[pd.Series, pd.DataFrame]:
        """Return the average posterior prediction across all samples.
        
        Parameters
        ----------
        df : pd.DataFrame
            Source dataframe.
        ci : float
            Option to include a credible interval around the predictions. Returns a 
            dataframe if true, a series if false. Default False.
        ci_interval : float
            Credible interval width. Default 0.9.
        aggfunc : string or callable
            Aggregation function called over predictions across posterior samples. 
            Applies only to the point prediction (not the CI).
        Returns
        -------
        pd.Series or pd.DataFrame
            Forecasts. Will be a series with the name of the dv if no ci. Will be a
            dataframe if ci is included.
        """
        # get aggfunc if a string
        if not callable(aggfunc):
            aggfunc = getattr(onp, aggfunc)

        transformed = self.transform(df)

        # check for nulls
        null_cols = columns_with_null_data(transformed)
        if null_cols:
            raise NullDataFound(*null_cols)

        # matmul inputs * coefs, then send through link
        predictions = self.link(transformed.values @ self.samples_df.transpose().values)
        yhat = aggfunc(predictions, axis=1)

        if not ci:
            return pd.Series(yhat, index=df.index, name=self.dv)

        quantiles = onp.quantile(predictions, [1 - ci_interval, ci_interval], axis=1)
        return pd.DataFrame(
            {self.dv: yhat, "ci_lower": quantiles[0, :], "ci_upper": quantiles[1, :],},
            index=df.index,
        )

    @require_fitted
    def sample_posterior_predictive(
        self,
        df: pd.DataFrame,
        hdpi: bool = False,
        hdpi_interval: float = 0.9,
        rng_key: np.ndarray = None,
    ) -> typing.Union[pd.Series, pd.DataFrame]:
        """Obtain samples from the posterior predictive.
        
        Parameters
        ----------
        df : pd.DataFrame
            Source dataframe.
        hdpi : bool
            Option to include lower/upper bound of the highest posterior density 
            interval. Returns a dataframe if true, a series if false. Default False.
        hdpi_interval : float
            HDPI width. Default 0.9.
        rng_key : two-element ndarray.
            Optional rng key, will be randomly splitted if not provided.
        Returns
        -------
        pd.Series or pd.DataFrame
            Forecasts. Will be a series with the name of the dv if no HDPI. Will be a
            dataframe if HDPI is included.
        """
        # get rng key
        rng_key_ = (
            self.split_rand_key() if rng_key is None else rng_key.astype("uint32")
        )

        # check for nulls
        null_cols = columns_with_null_data(self.transform(df))
        if null_cols:
            raise NullDataFound(*null_cols)

        #  do it
        predictions = infer.Predictive(self.model, self.samples_flat)(rng_key_, df=df)[
            self.dv
        ]

        if not hdpi:
            return pd.Series(predictions.mean(axis=0), index=df.index, name=self.dv)

        hdpi = diagnostics.hpdi(predictions, hdpi_interval)

        return pd.DataFrame(
            {
                self.dv: predictions.mean(axis=0),
                "hdpi_lower": hdpi[0, :],
                "hdpi_upper": hdpi[1, :],
            },
            index=df.index,
        )

    @property
    @require_fitted
    def num_samples(self):
        """Return the number of samples per variable.
        
        Assumes samples from all variables have same shape. Counts samples across all
        chains.
        """
        k = next(self.features.__iter__())
        return np.prod(np.array(self.samples[k].shape))

    @property
    @require_fitted
    def num_chains(self) -> int:
        """Return the number of chains per variable in the model.
        
        Assumes samples from all variables have same shape.
        """
        k = next(self.features.__iter__())
        return self.samples[k].shape[0]

    @property
    @require_fitted
    def samples_flat(self):
        """Provide a 1D view of the model's samples."""
        return {k: v.flatten() for k, v in self.samples.items()}

    @property
    @require_fitted
    def samples_df(self) -> pd.DataFrame:
        """Return a DataFrame of the model's MCMC samples."""
        num_chains, num_samples = self.num_chains, self.num_samples
        samples_per_chain = num_samples / num_chains
        index = pd.MultiIndex.from_product(
            [
                np.arange(num_chains, dtype="uint32"),
                np.arange(samples_per_chain, dtype="uint32"),
            ],
            names=["chain", "sample"],
        )
        return pd.DataFrame(self.samples_flat, index=index)[self.features.keys()]

    @classmethod
    def from_dict(cls, data: typing.Dict[str, typing.Any], **model_kw):
        """Return a pre-fitted model given a dictionary of config.
        The dictionary MUST contain the following:
        - samples. A dictionary of variables to MCMC samples. Must contain all feature 
        names and additional model variables. Each variable's data must be the same 
        shape.
        Any other dict keys will be added as model attributes.
        
        Parameters
        ----------
        data : dict.
            Model configuration, including requirements listed above.
        kwargs
            passed to Model() init.
    
        Returns
        -------
        Model
            A ready-to-use model.
        """
        data = cls.preprocess_config_dict(data)
        model = cls(**model_kw)
        model.fitted = True

        # assign dict keys to model
        for k, v in data.items():
            setattr(cls, k, v)

        return model

    @require_fitted
    def to_json(self) -> str:
        """Return a JSON payload of the model's config."""
        return json.dumps({"samples": self.samples}, cls=NumpyEncoder)

    @classmethod
    def preprocess_config_dict(cls, config: dict) -> dict:
        """Run checks and transformations on dicts for use in ``from_dict()``."""
        # make samples into jax arrays
        samples = {k: device_put(np.array(v)) for k, v in config["samples"].items()}

        # check that all keys are there
        for name in list(cls.features.keys()) + cls._additional_variables:
            if name not in samples:
                raise IncompleteSamples(name)

        # check that all samples have the same shape
        shape = None
        for k, v in samples.items():
            _shape = v.shape
            shape = _shape if shape is None else shape
            if (shape != _shape) or (len(_shape) != 2):
                raise IncompleteSamples(k)

        # samples check out, so reassign
        config["samples"] = samples
        return config

    @require_fitted
    def metrics(
        self, df: pd.DataFrame, aggerrs: bool = True
    ) -> typing.Union[pd.DataFrame, typing.Dict[str, float]]:
        """Get prediction accuracy metrics of the model against data.
        
        Parameters
        ----------
        df : pd.DataFrame
            Input data for the model.
        aggerrs : bool
            Option to aggregate errors across observations (default True). If true, 
            a dictionary of summary statistics are returned. If False, pointwise errors
            are returned as a DataFrame.
        
        Returns
        -------
        dict or pd.DataFrame
            If aggerrs, a dictionary of summary statistics are returned. If False, 
            pointwise errors are returned as a DataFrame.
        """
        y = df[self.dv]
        yhat = self.predict(df)
        if aggerrs:
            return metrics(y, yhat)

        return pd.DataFrame(dict(residual=y - yhat), index=df.index).assign(
            pe=lambda x: x.residual / y * 100, ape=lambda x: onp.abs(x["pe"]),
        )

    @require_fitted
    def grouped_metrics(
        self,
        df: pd.DataFrame,
        groupby: typing.Union[str, typing.List[str]],
        aggfunc: typing.Callable = onp.sum,
        aggerrs: bool = True,
    ) -> typing.Union[pd.DataFrame, typing.Dict[str, float]]:
        """Return grouped accuracy metrics.
        
        Parameters
        ----------
        df : pd.DataFrame
            Input data for the model.
        groupby : str or list of str
            Groupby clause for pandas.
        aggfunc : callable
            How to aggregate actuals and predictions wihtin a group. Default sum.
        aggerrs : bool
            Option to aggregate errors across groups (default True). If true, 
            a dictionary of summary statistics are returned. If False, groupwise errors
            are returned as a DataFrame.
        
        Returns
        -------
        dict or pd.DataFrame
            If aggerrs, a dictionary of summary statistics are returned. If False, 
            groupwise errors are returned as a DataFrame.
        """
        # aggregate per group
        res = (
            df.assign(_yhat=self.predict)
            .groupby(groupby)
            .agg(**{"y": (self.dv, aggfunc), "yhat": ("_yhat", aggfunc),})
            .assign(
                residual=lambda x: x.yhat - x.y,
                pe=lambda x: x.residual / x.y * 100,
                ape=lambda x: onp.abs(x["pe"]),
            )
        )

        if not aggerrs:
            return res[["residual", "pe", "ape"]]
        return metrics(res.y, res.yhat)

    @property
    @require_fitted
    def formula(self):
        """Return a formula string describing the model."""
        descriptives = self.samples_df.describe()
        formula_template = f"{self.dv} = " + self._formula_link_str

        # get a string rep from each descriptive column. this will be for each feature:
        #       x * mu(+-sd)
        def get_str(x):
            mu = x["mean"]
            sd = x["std"]
            if x.name == descriptives.columns.values[0]:
                prefix = "    "
            else:
                prefix = "  + "
            return prefix + f"""{x.name} * {mu:0.5f}(+-{sd:0.5f})"""

        lc = "\n".join(descriptives.apply(get_str, axis=0).tolist())
        return formula_template.format(lc=lc)


class Normal(BaseModel):
    """Gaussian/normal family model for the generic regression model."""

    sigma_prior = 1.0
    _additional_variables = ["_sigma"]

    @staticmethod
    def link(x):
        """Linear link function."""
        return x

    def likelihood_func(self, yhat):
        """Return a normal likelihood with fitted sigma."""
        _sigma = numpyro.sample("_sigma", dist.Exponential(self.sigma_prior))
        return dist.Normal(yhat, _sigma)


class Poisson(BaseModel):
    """Exponential/poisson family model for rate data."""

    _formula_link_str = "exp(\n{lc}\n)"

    @staticmethod
    def link(x):
        """Exponential link function."""
        return np.exp(x)

    def likelihood_func(self, yhat):
        """Return a poisson likelihood."""
        return dist.Poisson(yhat)


class Bernoulli(BaseModel):
    """Logistic/bernoulli family model, for a binary response variable."""

    _formula_link_str = "logistic(\n{lc}\n)"

    @staticmethod
    def link(x):
        """Logistic link function."""
        return expit(x)

    def likelihood_func(self, probs):
        """Return a Bernoulli likelihood."""
        return dist.Bernoulli(probs=probs)









#########################################################################################
"""Custom errors for shabadoo models."""
class ShabadooException(Exception):
    """Parent class for """

    def __str__(self):
        """Return the exception string."""
        name = self.__class__.__name__
        message = self.message or ""
        return f"{name}({message})"


class NotFittedError(ShabadooException):
    """Raised when using post-fit model functionality on an unfitted model."""

    def __init__(self, func=None):
        """Set the message."""
        name = func.__name__ if func else "function"
        self.message = f"Unable to call {name} before fitting model."


class AlreadyFittedError(ShabadooException):
    """Raised when calling fit on a fitted model."""

    def __init__(self, model):
        """Set the message."""
        name = model.__class__.__name__
        self.message = f"Model {name} has already been fitted!"


class IncompleteModel(ShabadooException):
    """Raised when initializing a model with missing config."""

    def __init__(self, model, attribute):
        """Set the message."""
        name = model.__class__.__name__
        self.message = f"Model `{name}` does not have attribute `{attribute}`!"


class IncompleteFeature(ShabadooException):
    """Raised when initializing a model with an incomplete feature."""

    def __init__(self, name, key):
        """Set the message."""
        self.message = f"Feature `{name}` does not have a {key}!"


class IncompleteSamples(ShabadooException):
    """Raised a model has incomplete samples for some reason."""

    def __init__(self, name):
        """Set the message."""
        self.message = f"No or not enough samples found for `{name}`."


class NullDataFound(ShabadooException):
    """Raised when passing null data to fit/predict."""

    def __init__(self, *names):
        """Set the message."""
        self.message = f"Null data detected in features: {', '.join(names)}."