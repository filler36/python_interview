"""
Positional-only arguments / Positional or keyword arguments
Positional or keyword arguments	* Keyword-only arguments
"""
def foo(pos1, pos2, /, pos_or_kwd1, pos_or_kwd2='default', *args, kwd_only1, kwd_only2='default', **kwargs):
    print(
        f"pos1={pos1}",
        f"pos2={pos2}",
        f"pos_or_kwd1={pos_or_kwd1}",
        f"pos_or_kwd2={pos_or_kwd2}",
        f"args={args}",
        f"kwd_only1={kwd_only1}",
        f"kwd_only2={kwd_only2}",
        f"kwargs={kwargs}",
        sep="\n",
    )
foo(1, 2, 3, 4, 5,6,7, kwd_only1=8, kwd_only2='9', a=10, b=11)
