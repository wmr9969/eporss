------------------------------------------------------------------------------------------
	                   Readme for the EPORSS algorithm Package
	 		                version May 6, 2022
------------------------------------------------------------------------------------------

General information:

This package includes the python code of the paper [1].

[1] Chao Bian, Yawen Zhou, and Chao Qian. Robust Subset Selection by Greedy and Evolutionary Pareto Optimization. In: Proceedings of the 31st International Joint Conference on Artificial Intelligence (IJCAI'22), Vienna, Austria, 2022.


*************************************************************
Environment requirement:

    python >= 3.7
    numpy == 1.19.2

*************************************************************
Descriptions

algorithms.py: The implementation of the EPORSS, Greedy, Modified greedy, and SATURATE algorithm.

select_nodes_as.py: Generate subgraph that includes the 200 most active nodes of the 6 graphs in dataset as-733.

select_nodes_fb.py: Generate subgraph that includes the 200 most active nodes of the dataset facebook.

generate_probs_fb.py: Generate 6 different probabilities settings of subgraph of the dataset facebook.

run_as.py: Test algorithms in subgraphs of as-733.

run_fb.py: Test algorithms in subgraphs of facebook.

datasets/: Directory containing the dataset as-733 and facebook.

*************************************************************
Usage
-------------------------------------------------------------
as-733:
You can test algorithms in subgraphs of as-733 via running the following commands:

    $ python select_nodes_as.py

    $ python run_as.py
    optional arguments:
      -h, --help       show this help message and exit
      --k K            Budget k
      --m {2,3,4,5,6}  Objectives m
      --t T            Index of this run of the k,m setting

The results will be saved in directory output/output_as/.
-------------------------------------------------------------
facebook:
You can test algorithms in subgraphs of facebook via running the following commands:

    $ python select_nodes_fb.py

    $ python generate_probs_fb.py

    $ python run_fb.py
    optional arguments:
      -h, --help       show this help message and exit
      --k K            Budget k
      --m {2,3,4,5,6}  Objectives m
      --t T            Index of this run of the k,m setting

The results will be saved in directory output/output_fb/.
*************************************************************

ATTN: 
- This package is free for academic usage. You can run it at your own risk. For other purposes, please contact Dr. Chao Qian (qianc@lamda.nju.edu.cn).

- This package was developed by Mr. Chao Bian (bianc@lamda.nju.edu.cn) and Ms. Yawen Zhou (zyw8769@gmail.com). For any problem concerning the code, please feel free to contact them.
