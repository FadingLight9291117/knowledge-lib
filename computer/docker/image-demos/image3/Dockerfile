FROM nginx:alpine
LABEL maintainer="CLZ <clz@clz.com>"

ENV NGX_DOC_ROOT="/data/web/html"

ADD index.html ${NGX_DOC_ROOT}
ADD entrypoint.sh /bin/

CMD ["/usr/sbin/nginx", "-g", "daemon off"]
ENTRYPOINT ["/bin/entrypoint.sh"]
