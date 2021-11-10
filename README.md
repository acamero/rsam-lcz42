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

1. Get the code `git clone https://github.com/acamero/rsam-lcz42-2021.git`, and go to the *new* folder (`cd rsam-lcz42-2021`);

2. Create a virtual environemnt (**Recommended**) `virtualenv --python=python3.8 venv`, and activate it `source venv/bin/activate`;

3. Install *Jupyterlab* `pip install jupyterlab`, and start it `jupyter-lab` (a new browser window will open);

4. Download the data from [LINK](https://syncandshare.lrz.de/getlink/fi3eWuN4bgAnaExzushQUahm/subset_lcz42.h5), and copy to the data folder `rsam-lcz42-2021/data`;

5. Open the notebook `lcz42_intro.ipynb`, and follow the instructions.
