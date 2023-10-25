# Remote Sensing Advanced Methods


## So2Sat LCZ42

By 2050, Berlin summers could be as hot as in Canberra, Australia. Pankow, a district in the city’s north, has already declared a climate emergency in 2019 and is planning ahead. It is planting trees from the Mediterranean that can withstand the heat, and has calculated computer simulations for sunshine and cold air corridors for the construction of 1200 new apartments. A few changes, like swapping asphalt and concrete that store heat against greenery that soaks up water and provides shade, can make a difference on the local scale. Many of these changes on a local scale then make a difference on the bigger scale.

To understand local climate in cities, scientists have developed the Local Climate Zone classification scheme, as part of the So2Sat project. The aim is to create a 4D urban map of the world.

It differentiates between 17 zones based mainly on surface structures (such as building and tree density) as well as surface cover (green, pervious soils versus impervious grey surfaces). There are algorithms that calculate these maps from freely available satellite imagery, but there’s still room for improvement by adapting or developing suitable and advanced Convolutional Neural Network (CNN) architectures that generalise well.

The outcome of So2Sat will be the first and unique global and consistent spatial data set on urban morphology (3D/4D) of settlements, and a multidisciplinary application derivate assessing population density. This is seen as a giant leap for urban geography research as well as for formation of opinions for stakeholders based on resilient data.

```
@article{zhu2020so2sat,
  title={So2Sat LCZ42: a benchmark data set for the classification of global local climate zones [Software and Data Sets]},
  author={Zhu, Xiao Xiang and Hu, Jingliang and Qiu, Chunping and Shi, Yilei and Kang, Jian and Mou, Lichao and Bagheri, Hossein and Haberle, Matthias and Hua, Yuansheng and Huang, Rong and others},
  journal={IEEE Geoscience and Remote Sensing Magazine},
  volume={8},
  number={3},
  pages={76--89},
  year={2020},
  publisher={IEEE}
}
```

## Getting Started

To start from scratch, please follow the steps:

1. Check that you have `python` installed in your system. Open a terminal (*power shell* in Windows), and then type:

```
python --version
```

You should see something like `Python 3.8.0`. This tutorial requires `python >= 3.8`. If you don't have python installed, visit [python.org](https://www.python.org/downloads/), and follow the instructions.


2. Get the code `git clone https://github.com/acamero/rsam-lcz42-2021.git`, and go to the *new* folder (`cd rsam-lcz42-2021`);

3. (**Recommended**) Create a virtual environemnt `virtualenv --python=python3.8 venv`, and activate it `source venv/bin/activate`;

4. Install *Jupyterlab* `pip install jupyterlab`;

5. Download the data from [link](https://syncandshare.lrz.de/getlink/fi3eWuN4bgAnaExzushQUahm/subset_lcz42.h5), and copy to the data folder `rsam-lcz42-2021/data`;

6. Start *Jupyterlab* `jupyter-lab` (a new browser window will open), open the *notebook* `lcz42_intro.ipynb`, and follow the instructions.

**Note**: Please, be sure to complete steps 1 to 5 before the lecture, and to install all the required packages, either by running the first block of code of the notebook, or by executing `pip install -r requirements.txt`. Then, check that everything is ready by running `python check.py`. If the required packages are installed and the data is in place, you will get an `OK`.

