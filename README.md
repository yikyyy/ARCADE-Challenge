# ARCADE-Challenge

## Official website of challenge:
[arcade.grand-challenge.org](https://arcade.grand-challenge.org/)

## Instruction
- Before training, use the code in "prep_training" to pre-process the dataset.
- Preprocessing consists of 1) converting coco format annotations to mask format 2) classifying the dataset according to the definition of coronary artery 3) ensuring that there are 4 training sets capable of training 4 models.
- Training through nnU-Net default configuration.
- Once training is complete, inference can be performed with the code in the home directory (encapsulated as a docker image).
