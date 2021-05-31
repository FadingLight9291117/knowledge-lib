FROM busybox

ENV WEB_DOC_ROOT=/data/html

RUN mkdir -p ${WEB_DOC_ROOT} && \
    echo "<h1>hello</h1>" > ${WEB_DOC_ROOT}/index.html

ENTRYPOINT httpd -f -h ${WEB_DOC_ROOT}
