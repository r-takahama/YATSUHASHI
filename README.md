# Which is the Best Yatsuhashi Brand for a Souvenir?

Experiments for the technical paper [Which is the Best Yatsuhashi Brand for a Souvenir? (私たちはお土産にどの八ッ橋を買えばよいのか)](http://www.ml.ist.i.kyoto-u.ac.jp/wp/wp-content/uploads/2014/10/yatsuhashi.pdf).

## Dependencies
- Python 3.5
- numpy 1.11.1
- scipy 0.17.1

## Usage
Clone this repository:
```bash
$ git clone https://github.com/r-takahama/YATSUHASHI.git
```

Move working directory:
```bash
$ cd YATSUHASHI/src
```

Run python code for checking the result of experiments:
```bash
$ python calcScore.py
```

And you will obtain the following output:
```bash
Results of primary eigenvector:
Score of Yatsuhashi y1 = 0.119
Score of Yatsuhashi y2 = 0.364
Score of Yatsuhashi y3 = 0.156
Score of Yatsuhashi y4 = 0.334
Score of Yatsuhashi y5 = 0.462
Score of Yatsuhashi y6 = 0.249
Score of Yatsuhashi y7 = 0.302
Score of Yatsuhashi y8 = 0.355
Score of Yatsuhashi y9 = 0.212
Score of Yatsuhashi y10 = 0.082
Score of Yatsuhashi y11 = 0.416

Results of Bradley-Terry model:
Score of Yatsuhashi y1 = -1.039
Score of Yatsuhashi y2 = 0.501
Score of Yatsuhashi y3 = -0.895
Score of Yatsuhashi y4 = 0.562
Score of Yatsuhashi y5 = 1.200
Score of Yatsuhashi y6 = -0.061
Score of Yatsuhashi y7 = 0.158
Score of Yatsuhashi y8 = 0.715
Score of Yatsuhashi y9 = -0.228
Score of Yatsuhashi y10 = -1.806
Score of Yatsuhashi y11 = 0.892

Results of Crowd-BT model:
Score of Yatsuhashi y1 = -0.540
Score of Yatsuhashi y2 = 1.549
Score of Yatsuhashi y3 = -2.905
Score of Yatsuhashi y4 = 0.631
Score of Yatsuhashi y5 = 3.328
Score of Yatsuhashi y6 = 0.020
Score of Yatsuhashi y7 = 1.847
Score of Yatsuhashi y8 = 1.412
Score of Yatsuhashi y9 = -0.434
Score of Yatsuhashi y10 = -5.993
Score of Yatsuhashi y11 = 6.468
Eta of Worker a1 = 1.000
Eta of Worker a2 = 0.808
Eta of Worker a3 = 1.000
Eta of Worker a4 = 0.418
Eta of Worker a5 = 0.580
Eta of Worker a6 = 0.944
Eta of Worker a7 = 0.440
Eta of Worker a8 = 0.869
Eta of Worker a9 = 1.000
```

You are also able to check the implementation of experimental calcuration by seeing `calcScore.py`.
