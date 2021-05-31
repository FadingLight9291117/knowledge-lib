#!/bin/sh
# 
cat > /etc/nginx/conf.d/www.conf << EOF
servser { 
	server_name $HOSTNAME;
	listen ${IP:-0.0.0.0}:${PORT:-80};
	root ${NGX_DOC_ROOT};
}
EOF

# 替换shell
exec "$@"
