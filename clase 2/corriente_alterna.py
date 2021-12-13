s = input()
st = []
for x in s:
    if not st or st[-1] != x:
        st.append(x)
    else:
        st.pop()
if st:
    print('No')
else:
    print('Yes')