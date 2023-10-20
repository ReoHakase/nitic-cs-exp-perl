# 情報工学実験 III Perl / CGI 演習

令和 5 年度開講

## CGI プログラムの実行方法

### `counter.cgi`

Web ページの表示回数をカウントするためには、カウントデータを保存するファイルが必要です。以下に基本的な Perl CGI プログラムを示します。このプログラムは、カウンタファイルを読み、カウントを増やし、更新されたカウントをファイルと Web ページに書き戻します。

- `src/counter.cgi`

```perl
#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);

# カウンタファイルのパスを指定
my $counter_file = 'counter.txt';

# カウントを取得および更新
open my $fh, '+<', $counter_file or die "Can't open $counter_file: $!";
my $count = <$fh>;
$count = 0 unless defined $count;
$count++;
seek $fh, 0, 0;
print $fh $count;
close $fh;

# HTMLページを出力
print header;
print start_html('Counter Page');
print "This page has been viewed $count times.";
print end_html;
```

この CGI プログラムを実行するには、以下の手順を実行します：

1. ~~**プログラムの保存**~~:

   - ~~上記のコードを`counter.cgi`という名前のファイルに保存します。~~

2. **実行権限の設定**:

   - プログラムファイルに実行権限を付与します。ターミナルを開いて、以下のコマンドを実行します：
     ```bash
     chmod +x src/counter.cgi
     ```

3. **XAMPP の設定**:

   - XAMPP を開き、Apache Web サーバーを起動します。

4. **CGI ディレクトリの設定**:

   - XAMPP の設定ファイル（通常は`/Applications/XAMPP/etc/httpd.conf`）をエディタで開き、以下のように CGI ディレクトリを設定します：
     ```plaintext
     <Directory "/Applications/XAMPP/cgi-bin">
         AllowOverride None
         Options ExecCGI
         Order allow,deny
         Allow from all
     </Directory>
     ```

5. **プログラムの配置**:

   - counter.cgi`ファイルを`/Applications/XAMPP/cgi-bin`ディレクトリにコピーします。
   - シンボリックリンクを使用しても動作します。`/Applications/XAMPP/cgi-bin`ディレクトリ内に`counter.cgi`へのシンボリックリンクを作成することで、実際の`counter.cgi`ファイルが他の場所にある場合でも、XAMPP の Apache サーバーはそれを正しく認識し実行することができます。
     シンボリックリンクを作成するには、ターミナルを開き、以下のコマンドを実行します（実際の`counter.cgi`ファイルのパスと、リンクの目的地を適切に置き換えてください）: `$ ln -s src/counter.cgi /Applications/XAMPP/cgi-bin/counter.cgi`

このコマンドは`/Applications/XAMPP/cgi-bin`ディレクトリ内に`counter.cgi`という名前のシンボリックリンクを作成し、このリンクは実際の`counter.cgi`ファイルを指します。その後、Web ブラウザを使って`http://localhost/cgi-bin/counter.cgi`にアクセスすることで、CGI プログラムを実行することができます。

1. **Web ブラウザでアクセス**:
   - Web ブラウザを開き、`http://localhost/cgi-bin/counter.cgi`にアクセスします。

以上で、カウンタプログラムが動作し、Web ページにアクセスするたびにカウントが増加するはずです。また、カウンタ値は`counter.txt`ファイルに保存され、プログラムはそのファイルからカウント値を読み取ります。
