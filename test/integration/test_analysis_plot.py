# coding: utf-8

"""
Corresponds to "Register and store an analysis plot created in the notebook into KG"
"""

import os
import matplotlib.pyplot as plt
import numpy as np

from fairgraph import KGClient
from fairgraph.brainsimulation import AnalysisResult

import pytest


token = os.environ.get("HBP_AUTH_TOKEN", None)

if token:
    client = KGClient(token, nexus_endpoint="https://nexus-int.humanbrainproject.org/v0")


@pytest.mark.skip("comment this out to run the test")
@pytest.mark.skipif(token is None,
                    reason="No token provided. Please set environment variable HBP_AUTH_TOKEN")
def test_all():

    ## Create a fake analysis plot as an example

    if not os.path.isdir("results"):
        os.makedirs("results")

    time = np.linspace(0, np.pi*4, 100)
    signal = 1 + np.sin(time)

    plt.plot(time, signal)
    plt.xlabel("Time (ms)")
    plt.ylabel("Current (nA)")
    plt.title("Example data analysis plot")
    plt.savefig("results/example_data_analysis_plot.png")

    ## Register and store plot into KG

    result = AnalysisResult("Example data analysis plot", result_file="results/example_data_analysis_plot.png")
    result.save(client)
    result.timestamp

    ## Retrieve the plot from the KG

    if not os.path.isdir("retrieved_results"):
        os.makedirs("retrieved_results")

    results = AnalysisResult.by_name("Example data analysis plot", client, all=True)
    print(results)

    # alternatively
    print("Original uuid = " + result.uuid)
    result2 = AnalysisResult.from_uuid(result.uuid, client)
    print(result2)
    result2.download("retrieved_results", client)

    print(os.listdir("retrieved_results"))

    assert os.path.exists("retrieved_results/example_data_analysis_plot.png")
