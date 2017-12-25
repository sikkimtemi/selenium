# selenium
## 概要
Seleniumの環境構築が面倒だったため、Docker上で開発環境を再現できるように設定ファイルとサンプルスクリプトをまとめました。
`docker-compose up -d`するだけでSeleniumとPythonおよびHeadless Chromeの環境が出来上がります。ブラウザを用いた処理を自動化したい場合や、テスト自動化のベースとしてご利用ください。HeadlessなのでGUI環境のないサーバー上でも動作します。

## 事前準備
Dockerをインストールして、dockerコマンドとdocker-composeコマンドが使用できるようにしてください。

## 使い方
### インストールと起動方法

```bash
$ git clone https://github.com/sikkimtemi/selenium
$ cd selenium
$ docker-compose up -d
```

正常に起動できていれば下記のようになります。

```bash
$ docker-compose ps
    Name               Command           State           Ports
-----------------------------------------------------------------------
chrome         /opt/bin/entry_point.sh   Up      0.0.0.0:5900->5900/tcp
python         tail -f /dev/null         Up
selenium-hub   /opt/bin/entry_point.sh   Up      0.0.0.0:4444->4444/tcp
```

### 終了方法

```bash
$ docker-compose down
```

### サンプルスクリプトの実行

```bash
$ docker exec -it python /root/script/sample.py
```

実行するとGoogleにアクセスしてスクリーンショットを取得します。
script/imagesディレクトリに画像ファイルが保存されます。

### VNC接続によるデバッグ
`VNC`で接続するとブラウザの動きを確認しながらデバッグすることができます。Docker環境のIPアドレスにVNC(デフォルトは5900番ポート)でアクセスした上で、サンプルスクリプトを実行してみてください。デフォルトのパスワードは"secret"です。
