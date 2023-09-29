#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

# 设置算法镜像的内存限制为30GB。在Grand Challenge上，当前的内存限制是30GB，但可以在算法镜像设置中进行配置
MEM_LIMIT="30g"

# 这是固定的参数，还请不要改变，其主要功能为：在一系列限制的环境中运行名为grand_challenge_algorithm的镜像，并将本地路径和卷挂载到容器中供其访问
# --network="none"：禁用容器的网络功能，即容器内部无法访问网络
# --cap-drop="ALL"：禁用容器中的所有特权功能
# --security-opt="no-new-privileges"：禁止在容器内启用新的特权
# --shm-size="128m"：设置共享内存的大小为128MB
# --pids-limit="1024"：限制容器的进程数上限为1024个
# -v $SCRIPTPATH/test/:/input/images/coronary-angiography-x-ray-stack/：
# 将$SCRIPTPATH/test/本地路径挂载到容器中的/input/images/coronary-angiography-x-ray-stack/目录，因为本地测试的图像是在放在当前目录的test文件夹
# -v arcade-output-$VOLUME_SUFFIX:/output/：将名为arcade-output-$VOLUME_SUFFIX的Docker卷挂载到容器中的/output/目录
# grand_challenge_algorithm：指定要运行的镜像名称，如果之前的 ./build.sh 修改了镜象名词，这里还请同步修改，建议不修改
docker run --rm --gpus '"device=2"' \
        --memory="${MEM_LIMIT}" \
        --memory-swap="${MEM_LIMIT}" \
        --network="none" \
        --cap-drop="ALL" \
        --security-opt="no-new-privileges" \
        --shm-size="256m" \
        --pids-limit="1024" \
        -v $SCRIPTPATH/test/:/input/images/coronary-angiography-x-ray-stack/ \
        -v $SCRIPTPATH/:/output/ \
        grand_challenge_algorithm

# 上面这个命令，已经进行了调用了模型进行了预测，得到了最后的预测结果
