# Py

プログラミングテスト
Programming Test

お好きなプログラミング言語を解答して頂いて構いません。
Có thể sử dụng bất cứ ngôn ngữ yêu thích nào cũng được.
ヒントや用語などはWebで検索して頂いて構いません。
Bạn có thể tìm kiếm các gợi ý và thuật ngữ trên Web.
こちらで用意したテストケースに合格することに合わせて、ソースコードの書き方やコメントの入れ方、アルゴリズムなどを総合的に見させて頂きます。
Cùng với các test case mà chúng tôi đã chuẩn bị trước, chúng tôi sẽ xem xét toàn diện cách viết Source Code, cách comment, thuật toán (Algorithm), v.v.
設問に用意している「提出前の確認用テストケース」を必ず実行し、期待した結果になっていることを確認してから提出してください。
Hãy chắc chắn chạy hết các “Test case cần kiểm tra trước khi nộp bài” đã được chuẩn bị của đề bài, và chỉ nộp bài khi chắc chắn bài làm của mình sẽ ra được kết quả như mong đợi.  


カプレカ数  KAPREKAR number

標準入力から生の整数nが与えられるので、n以上かつnに一番近い値のカプレカ数を求め、標準出力に出力するプログラムを作成してください。
Với số nguyên n được nhập vào bằng cách nhập tiêu chuẩn (stdin), hãy viết chương trình để xuất ra dạng tiêu chuẩn (stdout) số Kaprekar lớn hơn hoặc bằng n và có giá trị gần với n nhất.

カプレカ数には2つの定義が存在しますが、この問題では下記の定義のことを指しています。
Có hai định nghĩa cho số Kaprekar, nhưng trong bài test này, chỉ đề cập đến định nghĩa sau.


整数の桁を並び替えて、最大にしたものと最小にしたものとの差を取る。この操作によって元の値に等しくなる数をカプレカ数と呼ぶ。
例えば、7641 – 1467 = 6174 であるから、6174はカプレカ数である。
この定義でのカプレカ数を小さい順に並べると以下のようになる。
0、495、6174、549945、631764、63317664、97508421、554999445、864197532 …
なお、カプレカ数は全て9の倍数である。
Sắp xếp các chữ số của một số nguyên để có hiệu số giữa số lớn nhất và số nhỏ nhất. Số tương đương với giá trị ban đầu bằng phép toán này được gọi là số Kaprekar.
Ví dụ, 7641 - 1467 = 6174, vì vậy 6174 là số Kaprekar.
Các số Kaprekar trong định nghĩa này được sắp xếp theo thứ tự tăng dần như sau.
0, 495, 6174, 549945, 631764, 63317664, 97508421, 554999445, 864197532…
Các số Kaprekar đều là bội số của 9.

例えば最初の数として2005を取り、上記の操作を繰り返すと
Ví dụ, nếu bạn lấy số đầu tiên là 2005, và lặp lại thao tác: 
5200 − 0025 = 5175
7551 − 1557 = 5994
9954 − 4599 = 5355
5553 − 3555 = 1998
9981 − 1899 = 8082
8820 − 0288 = 8532
8532 − 2358 = 6174
7641 − 1467 = 6174
となり、この後は 6174 が繰り返される。どのような4桁の数でも最終的に 0 または 6174 になることが確かめられる。
Thì sau đó, số 6174 sẽ được lặp lại. Ta có thể chắc chắn rằng bất kỳ chữ số nào có 4 chữ số cũng sẽ kết thúc bằng 0 hoặc 6174. 



なお、この問題では例えば上記に載っているカプレカ数の一覧など、既知のカプレカ数のテーブルを予め用意し、そこから近い値を走査する方法での解答は禁止とします。
Tuy nhiên, đối với bài test này, KHÔNG ĐƯỢC PHÉP ĐƯA RA C U TRẢ LỜI BẰNG CÁCH  chuẩn bị trước một bảng các số Kaprekar đã biết, chẳng hạn như danh sách các số Kaprekar được liệt kê ở trên và quét các giá trị gần với nó.


条件  Điều kiện
0 ≦ n ≦ 1,000,000,000


入力例 Ví dụ Input
100


出力例 Ví dụ output
495


問題文の条件に沿ってカプレカ数を出力してください。
Hãy tìm ra số Karprekar đáp ứng được điều kiện trên,

提出前の確認用テストケース     Các test case cần xác nhận trước khi nộp bài
Case 1) 100と入力した場合、495と出力される
Input 100, sẽ được output là 495
Case 2) 1000と入力した場合、6174と出力される
Input 1000, sẽ được output 6174
Case 3) 10000と入力した場合、549945と出力される
Input 10000, sẽ được output 549945
