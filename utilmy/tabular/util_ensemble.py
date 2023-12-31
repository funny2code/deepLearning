""" Ensembling

Docs ::

    https://deslib.readthedocs.io/en/latest/index.html

    Dynamic ensembling

    Welcome to DESlib documentation!
    =================================================

    DESlib is an ensemble learning library focusing the implementation of the state-of-the-art techniques for dynamic classifier
    and ensemble selection.

    DESlib is a work in progress. Contributions are welcomed through its GitHub page: https://github.com/scikit-learn-contrib/DESlib.

    Introduction
    --------------
    Dynamic Selection (DS) refers to techniques in which the base classifiers are selected
    on the fly, according to each new sample to be classified. Only the most competent, or an ensemble containing the most competent classifiers is selected to predict
    the label of a specific test sample. The rationale for such techniques is that not every classifier in
    the pool is an expert in classifying all unknown samples; rather, each base classifier is an expert in
    a different local region of the feature space.

    DS is one of the most promising MCS approaches due to the fact that
    more and more works are reporting the superior performance of such techniques over static combination methods. Such techniques
    have achieved better classification performance especially when dealing with small-sized and imbalanced datasets. A
    comprehensive review of dynamic selection can be found in the following papers [1]_ [2]_

    Philosophy
    -----------
    DESlib was developed with two objectives in mind: to make it easy to integrate Dynamic Selection algorithms to
    machine learning projects, and to facilitate research on this topic, by providing implementations of the main
    DES and DCS methods, as well as the commonly used baseline methods. Each algorithm implements the main methods
    in the scikit-learn_ API **scikit-learn**: **fit(X, y)**, **predict(X)**, **predict_proba(X)**
    and **score(X, y)**.

    The implementation of the DS methods is modular, following a taxonomy defined in [1]_.
    This taxonomy considers the main characteristics of DS methods, that are centered in three components:

    1. the methodology used to define the local region, in which the competence level of the base classifiers are estimated (region of competence);
    2. the source of information used to estimate the competence level of the base classifiers.
    3. the selection approach to define the best classifier (for DCS) or the best set of classifiers (for DES).

    This modular approach makes it easy for researchers to implement new DS methods, in many cases requiring only the
    implementation of the method **estimate_competence**, that is, how the local competence of the base classifier is measured.

    `API Reference <api.html>`_



"""