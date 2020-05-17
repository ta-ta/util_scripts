#!/usr/local/bin/zsh

# jupyter lab を起動停止する

# コマンドライン 引数の確認
if test $# -eq 0; then
    echo "how to use: bash jupyter_controller.sh (status|start|stop)"
    exit 0
fi
type=$1

if [ ${type} = "status" ]; then
    jupyter notebook list
elif [ ${type} = "start" ]; then
    dir=$2 # 指定しない場合は ~/ で start
    local=$3 # local で起動 引数を何か書く

    # ディレクトリの指定があるかを確認
    if [ -z ${dir} ]; then
        echo "invalid argument dir"
        exit 0
    fi

    # jupyter lab の起動
    echo "starting at cd ${dir}"
    if [ -n ${local} ]; then
        # local
        cd ${dir}
        nohup jupyter lab > jupyter.log 2>&1 &
    else
        # server
        cd ${dir}
        nohup jupyter lab --ip=0.0.0.0 --no-browser > jupyter.log 2>&1 &
    fi
elif [ ${type} = "stop" ]; then
    port=$2 # 指定しない場合は 8888 が stop
    if [ -z ${port} ]; then
        echo "invalid argument port"
        exit 0
    fi
    jupyter notebook stop ${port}
else
    echo "The command line argument can be choices from [status, start, stop]."
fi