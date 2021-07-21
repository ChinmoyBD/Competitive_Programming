t = int(input())
res_list = []
for _ in range(t):
    st_data = list(input().split())

    for i in range(1,4):
        a = float(st_data[i])
        st_data[i] = a
    res_list.append(st_data)
st_name = input().strip()
for i in range(len(res_list)):
    if res_list[i][0] == st_name:
        av_rs = (res_list[i][1] + res_list[i][2] + res_list[i][3]) / 3
        print("{:.2f}".format(av_rs))