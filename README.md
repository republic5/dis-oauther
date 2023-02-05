# Dis-oauther
![](https://img.shields.io/github/v/release/republic5/dis-oauther)
![](https://img.shields.io/github/license/republic5/dis-oauther)
![](https://github.com/republic5/dis-oauther/actions/workflows/codeql.yml/badge.svg)
![](https://img.shields.io/github/repo-size/republic5/dis-oauther)
![](https://img.shields.io/github/issues/republic5/dis-oauther)

This repository is a simple discord oauth implementation.<br/>
It is expected to be used for anti vpn and participation in the guild for authenticated users.<br/>
(日本語版は下部に記述しております)

## 1 Setup

- 1. Create bot <br />
  Go [here](https://discord.com/developers/applications) and click `New application`. <br/>
  And choose a name, agree to the [TOS](https://discord.com/developers/docs/policies-and-agreements/terms-of-service) and [Privacy](https://discord.com/developers/docs/policies-and-agreements/developer-policy), and create your bot.
  
- 2. Setting bot <br />
  Enable all Gateway Intents.
  
- 3. Edit config.yml <br />
  Open Config.<br />
  And, Press `Reset Token` from Bot and copy - paste.<br />
  Describe guild_id and role_id to assign a role.<br />
  > _This bot has Anti vpn functionality. If used, see section 2._
 
- 4. Make url <br />
  Go to `OAuth2`.<br />
  Copy the `CLIENT ID` and `CLIENT SECRET` from `Client information` and paste them into config.yml.<br />
  Then add the url you plan to forward to `Redirects` and add /login there.<br />
  The url should be pasted into the redirect_uri in config.yml.<br />
  Next, go to URL Generator from the left bar and select the url you just created from `SELECT REDIRECT URL`.<br />
  Also select a scope.<br />
  Copy the URL from the `GENERATED URL`.<br />
  This is important for login.<br />
  The selected `scope` is also stuck to the config.yml.<br />
  > _Example: identify%20guilds.join_
  
- 5.  Stating bot<br/>
  Install the package with `pip install -r requirements.txt`.<br />
  Finally, `python main.py` is used to start it up.
  
## 2 Anti vpn
Anti vpn by [getipintel](https://www.getipintel.net/).<br />
However, it is recommended to set `anti_vpn` to `false` when planning or scaling up large servers, as errors caused by rate limiting can cause problems.<br />
If used, anti_vpn must be set to true and email must be an email address that can receive email.

## 3 License
republic5 follows the [MIT license](https://github.com/republic5/dis-oauther/blob/main/LICENSE).

## 4 Join users together in a guild
  Let them join the guild from an authenticated user's access token.<br />
  To use it, open invite.py, specify the guild_id, and start it.<br />
  > _Conditionally, the bot must have the permission to invite the target user and the target bot must be a member of the guild._

## 5 Command
For commands, one is provided that creates an embed to be transferred to Url.<br />
`.button <embed_title> <embed_descriptor> <button_label> <url>`

## 6 Docker & k8s
Comming soon...

<hr>

# Dis-oauther
![](https://img.shields.io/github/v/release/republic5/dis-oauther)
![](https://img.shields.io/github/license/republic5/dis-oauther)
![](https://img.shields.io/github/repo-size/republic5/dis-oauther)
![](https://img.shields.io/github/issues/republic5/dis-oauther)

このリポジトリはディスコードでWeb認証するためのものです。<br />
アンチvpnや認証ユーザーのギルドへの参加などに利用されることが可能です。<br />
(English version is described at the top)

## 1 セットアップ

- 1. Botを作成する<br />
  [ここ](https://discord.com/developers/applications) に移動し、 `New application`を押します。<br />
  そして名前を選び、 [TOS](https://discord.com/developers/docs/policies-and-agreements/terms-of-service) と [Privacy](https://discord.com/developers/docs/policies-and-agreements/developer-policy)に同意しbotを作成します。
  
- 2. Botのセッティング<br />
  インデントをすべて有効にします。
  
- 3. config.ymlの編集 <br />
  コンフィグファイルを開いておきます。<br />
  そして、`Reset Token`を押して、コピー＆ペーストします。<br />
  ロールを割り当てるためにguild_idとrole_idを記述します。<br />
  > _もしAnti vpnの機能を使う場合、セクション2を参照ください。_
 
- 4. Urlの作成 <br />
  OAuth2に移動します。<br />
  `Client information`から`CLIENT ID`と`CLIENT SECRET`をコピーしてconfig.ymlに貼り付けます。<br />
  次に、`Redirects`に転送する予定のURLを追加し、そこに/loginを追加してください。<br />
  このurlはconfig.ymlのredirect_uriに貼り付けてください。<br />
  次に、左のバーから`URL Generator`に移動し、`SELECT REDIRECT URL`から先ほど作成したurlを選択します。<br />
  また、スコープも選択します。<br />
  `GENERATED URL`からURLをコピーします。<br />
  これはログイン時に必要です。<br />
  選択した`scope`もconfig.ymlに貼り付けます。<br />
  > _例: `identify%20guilds.join`_
  
- 5.  Botの起動<br />
  `pip install -r requirements.txt`でパッケージをインストールします。<br />
  最後に`python main.py`でBotを起動し、終了です。
  
## 2 Anti vpn
Anti vpn は [getipintel](https://www.getipintel.net/) を使用しております。<br />
ただし、レート制限によるエラーが問題を引き起こす可能性があるため、大規模なサーバーを計画または拡張する場合は、anti_vpn を false に設定することをお勧めします。<br />
もし使用する場合には、anti_vpnをtrueに設定し、emailはメールを受信できるメールアドレスである必要があります。

## 3 ライセンス
republic5は[MIT license](https://github.com/republic5/dis-oauther/blob/main/LICENSE)を尊重します。

## 4 ユーザーをサーバーに参加させる
認証されたユーザーのアクセストークンからギルドに参加させます。<br />
使用するには、invite.pyを開いてguild_idを指定し、起動します。<br />
> _条件として、ボットは対象のユーザーを招待する権限を持っている必要があり、また対象のボットはサーバーのメンバーである必要があります。_

## 5 コマンド
コマンドについては、Urlに転送させるための埋め込みを作成するものが用意されています。<br />
`.button <embed_title> <embed_descriptor> <button_label> <url>`

## 6 Docker & k8s
近日公開...
