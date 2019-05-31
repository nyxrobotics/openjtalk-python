#! /bin/sh

# openjtalkで音声合成を行うために必要なライブラリのインストールスクリプトです。
# Ubuntuを想定し、checkinstallコマンドを使用してインストールしています。
# (参考:https://server-setting.info/centos/open-jtalk-install.html )
# (参考:http://thr3a.hatenablog.com/entry/20180223/1519360909 )
# (参考:https://qiita.com/sukesuke/items/be2a4562bd809ccc0fab )
# (参考:http://april.fool.jp/blogs/2018/03/linux%E3%81%AB%E6%B3%A8%E6%96%87%E3%81%AE%E5%A4%9A%E3%81%84%E6%96%99%E7%90%86%E5%BA%97%E3%82%92%E3%81%97%E3%82%83%E3%81%B9%E3%82%89%E3%81%9D%E3%81%86%EF%BC%88open-jtalk%EF%BC%89/ )
# (参考:http://thr3a.hatenablog.com/entry/20180226/1519619690 )

now_dir=$PWD
mkdir -p ~/lib/openjtalk_libs
cd ~/lib/openjtalk_libs

# HTS Engine API のダウンロード&展開(検証済み：v1.10)
wget -O - 'http://downloads.sourceforge.net/hts-engine/hts_engine_API-1.10.tar.gz' | tar zxvf -
cd hts_engine_API-1.10
./configure
make
sudo checkinstall -y --pkgname='hts_engine_API' --pkgversion='1.10'
cd ..

# openjtalk本体のダウンロード&展開(検証済み：v1.11)
wget  -O - 'http://downloads.sourceforge.net/open-jtalk/open_jtalk-1.11.tar.gz' | tar zxvf -
cd open_jtalk-1.11
./configure \
--with-charset=utf-8
make
sudo checkinstall -y --pkgname='open_jtalk' --pkgversion='1.11'
cd ..

# openjtalk辞書ファイルのダウンロード(検証済み：utf8 v1.11)
wget -O - 'https://sourceforge.net/projects/open-jtalk/files/Dictionary/open_jtalk_dic-1.11/open_jtalk_dic_utf_8-1.11.tar.gz/download?use_mirror=jaist' | tar zxvf -

# MMDAgentの音声ファイルダウンロード(検証済み：v1.8)
wget 'https://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.8/MMDAgent_Example-1.8.zip'
unzip MMDAgent_Example-1.8.zip
rm MMDAgent_Example-1.8.zip

cd $now_dir