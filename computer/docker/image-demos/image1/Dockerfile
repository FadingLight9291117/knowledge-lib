# Description: test image

# FROM busybox@123

# FROM 必须是第一行，指定基础镜像
FROM busybox:latest

# MAINTAINER指定作者信息，已废除
MAINTAINER "clz <clz@clz.com>"

# 或者
LABEL maintainer="clz <clz@clz.com>"

# 环境变量
ENV DOC_ROOT=/data/web/html/ \
    WEB_SERVER_PACKAGE="nginx-1.15.2"

# COPY，复制主机文件到镜像中
COPY index.html /data/html/

# 指定存储卷
VOLUME /data/mysql/

# 可暴露端口
EXPOSE 80/tcp

# 改变当前工作目录
WORKDIR /usr/local/src/

# 类似COPY
ADD http://nginx.org/download/${WEB_SERVER_PACKAGE}.tar.gz ./src/

# `bulid`时运行命令
RUN cd /usr/local/src && \
    tar xf ${WEB_SERVER_PACKAGE} && \
    mv nginx-* webserver 

# run 时运行的命令
CMD /bin/httpd -f -h ${WEB_DOC_ROOT}
 
# 类似于CMD
ENTRYPOINT /bin/httpd -f -h ${WEB_DOC_ROOT}
