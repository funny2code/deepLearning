#!/usr/bin/env python3
import argparse
import sys
import os
import subprocess
import concurrent.futures
import time

PORT_START = 6370

def safe_system_exec(cmd: str, err_msg: str) -> None:
    """Try and execute a command, throw error with message on fail
    This is a bit grim but we need to execute shell commands. I.e `docker`
    :return: None
    """
    completed_process = subprocess.run(cmd, shell=True)
    if completed_process.returncode != os.EX_OK:
        raise Exception(err_msg)


def start_redis_server(port: int) -> None:
    """Execute shell command for starting a redis server
    port is the name of the directory
    :return: None
    """
    safe_system_exec(
        f"cd {port} && redis-server ./redis.conf",
        f"Failed to start redis server on port: {port}",
    )


def start_cluster(node_count: int) -> None:
    """Dynamically start a redis cluster
    :return: None
    """
    nodes = ""
    port = PORT_START
    for i in range(node_count):
        nodes += f"127.0.0.1:{port} "
        port += 1

    cmd = f"redis-cli --cluster create {nodes} --cluster-replicas 1 --cluster-yes"
    safe_system_exec(cmd, "Failed to create redis-cluster")


def create_conf(port: int) -> str:
    """Create redis conf in string buffer
    :return: str
    """
    return f"port {port}\ncluster-enabled yes\ncluster-config-file nodes.conf\ncluster-node-timeout 5000\nappendonly yes\n"


def create_nodes_config(node_count: int) -> None:
    """Create node_count number of redis nodes by creating a folder
    and writing a conf file
    :return: None
    """
    port = PORT_START
    for i in range(node_count):
        if not os.path.exists(f"{port}"):
            os.mkdir(f"{port}")
            f = open(f"./{port}/redis.conf", "w")
            f.write(create_conf(port))
            f.close()
        port += 1


def start_all_nodes(node_count: int) -> None:
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        port = PORT_START
        for i in range(node_count):
            executor.submit(start_redis_server, port=port)
            port += 1
        # Wait for nodes!
        time.sleep(5)
        start_cluster(node_count)
    concurrent.futures.wait(futures)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--node-count", type=int, required=True, help="How many redis nodes to create in cluster"
    )
    args = parser.parse_args(sys.argv[1:])
    create_nodes_config(args.node_count)
    start_all_nodes(args.node_count)

if __name__ == "__main__":
    main()
