
#!/bin/sh
# alias rm="sh /Users/Documents/script/git/remove.sh"

# 定义文件夹目录.Trash
TRASH_DIR="/Users/nijianfeng/.Trash"
# 定义秒时间戳
STAMP=`date +%s`
TARGET_DIR=$TRASH_DIR/$STAMP/
mkdir -p "$TARGET_DIR"
RECORD_FILE=$TARGET_DIR/.$STAMP.txt
touch "$RECORD_FILE"
for i in $*; do
    if [[ "$i" == -* ]];then
        echo do you want to remove "$i"
        read flag
        if [ "$flag" != "y" ];then
            continue
        fi
    fi
    echo "move $i to $TARGET_DIR >> $RECORD_FILE"
    echo "move $i to $TARGET_DIR" >> "$RECORD_FILE"
    # 将输入的参数对应文件mv至.Trash目录
    mv "$i" "$TARGET_DIR"
done