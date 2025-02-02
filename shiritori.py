def shiritori(names):
    # しりとりの先頭/末尾文字を取得する関数
    def get_char(name, reverse):
        # 長音と拗音と濁音/半濁音のリスト
        long_char = 'ー'
        small_chars = {
            'ァ': 'ア',
            'ィ': 'イ',
            'ゥ': 'ウ',
            'ェ': 'エ',
            'ォ': 'オ',
            'ッ': 'ツ',
            'ャ': 'ヤ',
            'ュ': 'ユ',
            'ョ': 'ヨ'
        }
        voiced_chars = {
            'ヴ': 'ウ',
            'ガ': 'カ', 'ギ': 'キ', 'グ': 'ク', 'ゲ': 'ケ', 'ゴ': 'コ',
            'ザ': 'サ', 'ジ': 'シ', 'ズ': 'ス', 'ゼ': 'セ', 'ゾ': 'ソ',
            'ダ': 'タ', 'ヂ': 'チ', 'ヅ': 'ツ', 'デ': 'テ', 'ド': 'ト',
            'バ': 'ハ', 'ビ': 'ヒ', 'ブ': 'フ', 'ベ': 'ヘ', 'ボ': 'ホ',
            'パ': 'ハ', 'ピ': 'ヒ', 'プ': 'フ', 'ペ': 'ヘ', 'ポ': 'ホ',
        }

        if reverse: # 末尾文字なら文字反転
            name = reversed(name)
        # 文字を探索
        for char in name:
            # 探索対象が長音記号なら次の文字へ
            if char == long_char:
                continue
            # 探索対象が拗音なら清音に戻してその文字を返却
            elif char in small_chars:
                return small_chars[char]
            # 探索対象が濁音/半濁音なら清音に戻してその文字を返却
            # 濁音/半濁音を別文字として扱うなら以下2行をアンコメント
            # elif char in voiced_chars:
            #     return voiced_chars[char]
            # 探索対象が長音でも拗音でも濁音/半濁音でもなければその文字を返却
            else:
                return char
        # 名前が全て長音なら何も返さない
        return None

    # 深さ優先探索を行う
    def dfs(current_name, used, path):
        # 名前を使用済みとする
        used.add(current_name)
        # パスに名前を追加
        path.append(current_name)

        # 接続する名前を探索
        for name in names:
            if name not in used and get_char(current_name, True) == get_char(name, False):
                dfs(name, used, path)

        # 長さが更新されたら記録
        if len(path) > len(longest_path[0]):
            longest_path[0] = path[:]

        # パスから名前を削除
        path.pop()
        # 名前を未使用に戻す
        used.remove(current_name)

    # 最長しりとりを格納する配列を用意
    longest_path = [[]]

    # 各名前から始まるしりとりを探索
    for name in names:
        print(f"Searching for starting from \"{name}\"")
        dfs(name, set(), [])

    # 最長しりとりを返却
    return longest_path[0]

# しりとりに用いる名前のリスト
names = ["スペシャルウィーク","サイレンススズカ","トウカイテイオー","マルゼンスキー","フジキセキ","オグリキャップ","ゴールドシップ","ウオッカ","ダイワスカーレット","タイキシャトル","グラスワンダー","ヒシアマゾン","メジロマックイーン","エルコンドルパサー","テイエムオペラオー","ナリタブライアン","シンボリルドルフ","エアグルーヴ","アグネスデジタル","セイウンスカイ","タマモクロス","ファインモーション","ビワハヤヒデ","マヤノトップガン","マンハッタンカフェ","ミホノブルボン","メジロライアン","ヒシアケボノ","ユキノビジン","ライスシャワー","アイネスフウジン","アグネスタキオン","アドマイヤベガ","イナリワン","ウイニングチケット","エアシャカール","エイシンフラッシュ","カレンチャン","カワカミプリンセス","ゴールドシチー","サクラバクシンオー","シーキングザパール","シンコウウインディ","スイープトウショウ","スーパークリーク","スマートファルコン","ゼンノロブロイ","トーセンジョーダン","ナカヤマフェスタ","ナリタタイシン","ニシノフラワー","ハルウララ","バンブーメモリー","ビコーペガサス","マーベラスサンデー","マチカネフクキタル","ミスターシービー","メイショウドトウ","メジロドーベル","ナイスネイチャ","キングヘイロー","マチカネタンホイザ","イクノディクタス","メジロパーマー","ダイタクヘリオス","ツインターボ","サトノダイヤモンド","キタサンブラック","サクラチヨノオー","シリウスシンボリ","メジロアルダン","ヤエノムテキ","ツルマルツヨシ","メジロブライト","デアリングタクト","サクラローレル","ナリタトップロード","ヤマニンゼファー","フリオーソ","トランセンド","エスポワールシチー","ノースフライト","シンボリクリスエス","タニノギムレット","ダイイチルビー","メジロラモーヌ","アストンマーチャン","サトノクラウン","シュヴァルグラン","ヴィルシーナ","ヴィブロス","ダンツフレーム","ケイエスミラクル","ジャングルポケット","ビリーヴ","ノーリーズン","スティルインラブ","コパノリッキー","ホッコータルマエ","ワンダーアキュート","サムソンビッグ","サウンズオブアース","ロイスアンドロイス","カツラギエース","ネオユニヴァース","ヒシミラクル","タップダンスシチー","ドゥラメンテ","ラインクラフト","シーザリオ","エアメサイア","デアリングハート","ブエナビスタ","オルフェーヴル","ジェンティルドンナ","ウインバリアシオン","ドリームジャーニー","カルストンライトオ","デュランダル","ハッピーミーク","ビターグラッセ","リトルココン","ヴェニュスパーク","リガントーナ","ソノンエルフィー","ライトハロー","ダーレーアラビアン","ゴドルフィンバルブ","バイアリーターク","モンジュー"]
# しりとりを探索
longest_shiritori = shiritori(names)
# 結果を出力
print("Result:")
print(" -> ".join(longest_shiritori), f"(len:{len(longest_shiritori)})")
