ARG PYTORCH="2.0.1"
ARG CUDA="11.7"
ARG CUDNN="8"

# Pull the docker image | 拉取镜像
FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel


# groupadd -r user => 创建了一个名为 "user" 的用户组
# useradd -m --no-log-init -r -g user user => 创建了一个名为 "user" 的用户，并将其添加到 "user" 用户组中
RUN groupadd -r user && useradd -m --no-log-init -r -g user user


# RUN mkdir .... => 创建了目录：/opt/app。选项-p表示如果父级目录不存在，也会创建它们
# chown user:user ... => 将创建的目录的所有者和组设置为user，以确保这些目录的访问权限是正确的，并且与容器内运行的进程用户匹配
RUN mkdir -p /opt/app \
    && chown user:user /opt/app


# 将当前Docker容器内的用户切换为 "user" 用户，并切换到 /opt/app 目录
USER user
WORKDIR /opt/app

ENV PATH="/home/user/.local/bin:${PATH}"

RUN python -m pip install --user -U pip  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com \
    && python -m pip install --user pip-tools -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


# Install the required packages
RUN pip install --user opencv-python -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com && \
    pip install --user geos -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com && \
    pip install --user shapely -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com \
    pip install --user opencv-python-headless -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


# 这个命令通过 COPY 指令将主机上的文件(夹)复制到容器中的 /opt/app/ 目录下，并指定文件(夹)的所有者和所属组为 user
COPY --chown=user:user DATASET /opt/app/DATASET
COPY --chown=user:user nnUNet /opt/app/nnUNet
COPY --chown=user:user process.py /opt/app/
COPY --chown=user:user 1_prep_data.py /opt/app/
COPY --chown=user:user 2_pred_trunk.py /opt/app/
COPY --chown=user:user 3_classification.py /opt/app/
COPY --chown=user:user 4_pred_rca.py /opt/app/
COPY --chown=user:user 5_pred_lcx.py /opt/app/
COPY --chown=user:user 6_pred_lad.py /opt/app/
COPY --chown=user:user 7_mask2coco.py /opt/app/
COPY --chown=user:user empty_annotations.json /opt/app/


# 切换到根据 nnUNet 的源码目录，从源码上安装 nnUNet 依赖包
WORKDIR /opt/app/nnUNet
RUN python -m pip install --user -e . -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


# Set environment variables | 设置环境变量
ENV nnUNet_raw="/opt/app/DATASET/nnUNet_raw" \
    nnUNet_preprocessed="/opt/app/DATASET/nnUNet_preprocessed" \
    nnUNet_results="/opt/app/DATASET/nnUNet_results"


# 在容器启动时执行命令
WORKDIR /opt/app
ENTRYPOINT [ "python", "-m", "process" ]