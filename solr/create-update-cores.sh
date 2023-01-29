#!/bin/bash
#
# create-update-cores.sh : run pre-create core if needed and copy/update schema and config files
#

repodir="/opt/solr-cores-repo"

if [[ -z $SOLR_HOME ]]; then
    coresdir="/opt/solr/server/solr/mycores"
else
    coresdir=$SOLR_HOME
fi

while read -r source ; do
    core=$(basename $source)
    target="$coresdir/$core"
    if [ -d "$target" ]; then
        echo "Found $core, updating schema and config"
    else
        /opt/docker-solr/scripts/precreate-core $core
    fi
    cp -av $source/* $target/conf
done < <(find $repodir -type d -maxdepth 1 -mindepth 1 ! -name .git)

