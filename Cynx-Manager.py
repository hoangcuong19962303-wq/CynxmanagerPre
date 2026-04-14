# -*- coding: utf-8 -*-
# Cynx Manager Premium - Developed By Cynx2502 (sieuthicloud247.com)
# Protected source code - Hardened Cross-Version Encrypted v2
# Copyright (c) 2024-2026 Cynx2502. All rights reserved.
# Tampering with this file will cause it to stop working.

import sys as gytuiwg1xy4ccn3np, os as v2igvkzkh6lwkfb

# === Anti-Debug & Anti-Tamper ===
def _d37t6b74tqewqc0p():
    try:
        import traceback as _tb
        aukke9crl1 = _tb.extract_stack()
        for eui4yh_uyxmfy0a in aukke9crl1:
            jn63lnp9y3zd394 = str(eui4yh_uyxmfy0a).lower()
            if 'uncompyle' in jn63lnp9y3zd394 or 'decompile' in jn63lnp9y3zd394 or 'dis.' in jn63lnp9y3zd394 or 'pydisasm' in jn63lnp9y3zd394 or 'pylingual' in jn63lnp9y3zd394 or 'pycdc' in jn63lnp9y3zd394:
                v2igvkzkh6lwkfb._exit(1)
    except:
        pass
    try:
        if hasattr(gytuiwg1xy4ccn3np, 'gettrace') and gytuiwg1xy4ccn3np.gettrace() is not None:
            v2igvkzkh6lwkfb._exit(1)
    except:
        pass
    try:
        if hasattr(gytuiwg1xy4ccn3np, 'getprofile') and gytuiwg1xy4ccn3np.getprofile() is not None:
            v2igvkzkh6lwkfb._exit(1)
    except:
        pass
_d37t6b74tqewqc0p()

# === Exec Guard: detect exec() hooking/replacement ===
def axay44nihscyp4s():
    """Verify exec and builtins have not been tampered with."""
    import builtins as lxlm3lneju94mu
    _jjjcjfirwztx9 = getattr(lxlm3lneju94mu, 'exec', None)
    if _jjjcjfirwztx9 is None:
        v2igvkzkh6lwkfb._exit(1)
    # Check exec is the real builtin, not a wrapper
    if hasattr(_jjjcjfirwztx9, '__module__') and _jjjcjfirwztx9.__module__ not in (None, 'builtins'):
        v2igvkzkh6lwkfb._exit(1)
    # Check if builtins.exec has been replaced
    if type(_jjjcjfirwztx9).__name__ != 'builtin_function_or_method':
        v2igvkzkh6lwkfb._exit(1)
    # Check compile hasn't been hooked
    _real_compile = getattr(lxlm3lneju94mu, 'compile', None)
    if _real_compile is None or type(_real_compile).__name__ != 'builtin_function_or_method':
        v2igvkzkh6lwkfb._exit(1)
    return _jjjcjfirwztx9
t9h3rnwlwpn9 = axay44nihscyp4s()

# === Frame inspection: detect if running inside hook ===
def i_ngb1vkh_2():
    try:
        import inspect
        for fi in inspect.stack():
            fn = fi.filename.lower() if hasattr(fi, 'filename') else str(fi[1]).lower()
            for bad in ['decode', 'hook', 'intercept', 'dump', 'extract', 'capture', 'inject', 'patch']:
                if bad in fn:
                    v2igvkzkh6lwkfb._exit(1)
    except:
        pass
i_ngb1vkh_2()

import zlib as _z, base64 as _b, hashlib as _h
def xlvjiyqw8dhfq(do6din4w62vwsy,m93j54b76gfz87wg):
    return bytes(bmbs0suiee0snh9lw6^m93j54b76gfz87wg[beo6ki9npzec2%len(m93j54b76gfz87wg)] for beo6ki9npzec2,bmbs0suiee0snh9lw6 in enumerate(do6din4w62vwsy))
def hrqq0lo4sg3_k6f(do6din4w62vwsy,m93j54b76gfz87wg):
    eimbmo7rr3ao0e4o5=_b.b85decode(do6din4w62vwsy)
    jn63lnp9y3zd394=xlvjiyqw8dhfq(eimbmo7rr3ao0e4o5,_b.b85decode(m93j54b76gfz87wg))
    return _z.decompress(jn63lnp9y3zd394)

tae5piwnplqry25="".join((
"T>Ib~xR=u`{{g4O$k`&(kO^(A*e!T=w(AnP(B@8-&XUW1Ho-WTMSOn~MDpETa$Objh=L!eQv55f*"
"H0l0u5BF#JoNhto7j;rA7&AEskF$zRA5=O65%O-;`ilaC4T7caVd@(fwwYsL{VRoj5UWb7QN1yLe"
"i~L<<KudC*uh_lm;@K=rD`uEmp#%aTZ`+I|<%;g2W_at#tY<L^s?XIvn>u@$fCxf(8^pyV@djInS"
"1R>ljnKCubbTqak4E`=3F$Eu+jQF}{Q3@h$tFUd^A0$SE^@o>bu8I!>6@e4?$D7)57q>uj;4)}9b"
"Fe}suekoQ7k)?dzo=rk}`4r5@4F_PMkMtzRd$4hwG&tG3MJr<97L8&okChv7LUmRPW*$i}okAj=n"
"pW!z3u@OimG6DG)c0a`^fuF_`1l_Mff5EZC$NJbP<S;${O8`6tJ;y!hZUsVaHyID5dtNx;eZY>CQ"
"5YFMX%Y|ok2+XRWa2=%+R^oy%jz?+y3#SF+VVr%uwC;6oc=Ip=eke;nVOFCHnWQEk%mq3E$VN18x"
"XlRCD~b<kMhj`ERrZcHvvDdYao5szEK*)JM<*Lvuh#+s#B>9RmRE1T}Q4?k7F3m_9nnZ9IiD)Mu="
"x#xs8eW8v!WcP8WaVbh3`DAl!yypNZ-iXd$@Z7n{h*mknsVJk1+%oEj*@?MccVwI{8mlJ^&KX9g("
"p@EFZ-TH`JjmW6c6$*NE2c$bz6?UUj-Bf0A@W(h^6<t7%r3!VJzf{7VYkEVn4TxZu@sC;(Vyz&UJ"
"^?V-^{dNvY&NzTE8rkA7O;OqstW0vF7(K`atd!)byHxs|0gL^oIs7zBK=7ZP9OlWLo`)WxC=dyJZ"
"THq1Y{+XVFUzlgEb4EmA24Gfx--FWw<|)$48#{Q(-5#3XZ0#=!vQZ!H!Xzf7VXTOS#?OK7_9GmoB"
"8sP3oWI`7KqONlh4bQfC`Iis{CUhOJD%b`I3A_WCK?9CH*DK9GO<oxs2qXakv-7U4Um>-g%JQ;N7"
"9@1aao#?%=szax|yP%y~-gNtFyrr~O&l_l_Rq6u4Ej+V_z3^Avd>k<`T;KEC*nfnT~;+v@WmTh(l"
"P8{%7)bA0cJ4GfFoz9H`-y|~X6J2{E<)Nrv5yabd@J!Fd6NuG0mWzIYfd!e8wF}76NC{t$K7j}(F"
"pBX_f{oBLX@C%n;vHWy}+L(-0YEzGAoVnF5xD;@3i|Y_HefYPV8JM1m<2l8bZ$g(7N!bv{<FI(Ws"
"Ne_k8~5j^ed3NtD9$eDesUEGuGWXA>EnfVagR19iH@PJHjQ1V#dA+~Xh#}w=X-&yZdDv2K!tJh<T"
"E0i9(hIzk92KBQ}QWZaC*m;tT4P@o~)X}FVv{X(QG6~YNEGl8u6ES{d?N2%tPkN@Z6l%3%y{|5O9"
"RP{0gkWbJ;e)JLb*KoGH1jM!C2*VJ4tSIb%B(KJ@(FARqJ5JcM17aXsPBuHQ+X{|+oLHLOw)ni++"
"}k;-lc3K}vO_GhRoja+?H=MB__;b}!Vr!teenon=>;<}pmiT`LH(^-y0Se%SpwY7g)#HUdSg0e6>"
"5;&?T8e&GFb>a7tr)OpQ#C{J8j>)*-$np_*X*m<tph(EBb~2Y`HMT+}rNcSH`c?U2XiVMSMuM+w4"
"Uj#mD|)Rz`wZ$Y>ozoFg;3<h#@05$K`^P5i%6s4hTvc2*SmrQjg+-#-3Uzr)1?KWwJ!}=9%rP&FK"
"-7fTL-EZnyQ8yP>rvgX)NYj`l6~NA@>`{4c%%_f*^Z8&0e_07gSW(J3zX_R5v5L5?V#YA)1GrghR"
"Fq+$76^$$EX~MRKq51IL)t5*UU$8Khr3%cA<}1&)S_ldE){YiZbCNz>NjZt*9zGOY0ugRl-`ym6M"
"1=))I_>+UAMnch2SS)n5Wu6ybzPEsuvLOyYzqo_7w9uap7cQPY6?hCuuspw9r3h8K)NPZMHMWS>e"
"FUv&q|1Qs~>=#tcGioXX7eOh)0~#EuxMtGw3ro@@x@3+UNr$*b?EY_UJ|H}18~?+m#Z^rJ8=|0a`"
"V1g692Dwov$4N7ye5`t+Q*&Jt@L4eE&g24k5$SdMK_<v{7-yMr!7P!2m(&U$>HpCv*ei5l?9Bxj{"
"PQu>NS;*O=;N1wJp!DS&xTMpFDqCU_!uMFd1q?Z$YBdqd3}w0E2tzbJ{7?Ztg=`LGd)m`|B6Aj*+"
"nZ#6`_Ft}dOpE?&$nSFvRMfiOdF&z>tX|NJY%W?19}u;iI6_iC3=A{vB5*WG*^k&}{TZ0GaJgPKO"
"?Flea<gr#!>miE`wtNIm6aTgCU_pN1qD=wXUDwes@UG`T|PRAOx&m7*O^Y82V!6ZeBt3Bh#P34LZ"
"$;)YOX7^R;Nzm}w$NYr{J@t964z%5c+^HT?L0&Ab?mFs$GNTVmpAzRDE4;&lA6F$|Vu>2W9I%Am&"
"Sk@+ydatUCT&lBYrD^UyE=j1pSz=s=^CI>7z=AG^-#I(i|&dw%M{d~OQe@Py|Fk^)J}xou;?%)Et"
"KT=GkQtr@??f}#sfN0?)>DC=P<NI6Am*(f{8y%_p}ZMW&`raYMd!t=EbFu?JxCjhG%{X*n2*uxn&"
"lS<*Fdnr_A6<f3n`5bg_0hx>)e=z_x^87e4Jq8m-|QBMm<ob``1IS)Xot`Se)185NS&tC`xg7bG-"
"6I@41N3z&J1yHbjHNFXOLu)vJOg8JHWR#ScCgjt}-ZX#LM5_o>>cQUlXtM(p)<dm?<$Uz!&I|X4o"
"1}94|hSLGa-YUfyoRkb9znV|L9s?GT&c6<O_7f)W&9J)$dfZTa5OP`4YA5_T&y<G0i?68xarXn*4"
"x_Q`vlaoahw)Rs66zarF&N0-wL_2&4-*>*nbtv7v9ZX0=88xtS4}daM6A)jR2CafpZtZH{Ru)Tgn"
"QN;VI_Z4{n`~=c3yMhw|R5sPnqt}${dTMRk%$Yx4T=Sx3k)S-mD=W4x;AM=sZRCFOB^y`~kX1b*S"
"36Im0`00e|5Og4oSTM5}fNk%Cvoj&^sy1CKIf&EKB=I?>?{_=r|(`n6-{7?aB-v^TCx$O%Bv5e>T"
"YY}l;sk^d|i`8Y)-38C|n<lv9?)aR?Jx?qrd;Huv$Qf2CN09;CPDX-9KnsS3?hrtZKv?9)>d!;!7"
"RraGIc>p%&3qO%szFFGi4mkpZ2$DE6DV^k`7F^AI^Bs{2oM;{*Qs(mnHJd7PFSm0aWUH`(Rtlvv6"
"wKcStUzmE38D^iigRFFbqB6B@O6!Gw9|eF(&5|aG*gt>>R?%K&de=Rc0k|VfCdnlmp4ZY<$dXYqN"
"99N{}D_GK1{+6CkPYa0}|Ziek?rL86G8DUHb-!8FcWk1~nxC6;YR^p(W7M4EN&s4u)_7A#tMj^QS"
"#{2%ZxO95knFo3M>;GubIrk;PQ)SgiKM!R>$NV3eREX9XrS48JFiQ7MJKMG?rzFI~oban+Y!;TE6"
"gKKJa@iJ`T4>#<!Y@hfb3x41EpWPa}z8J9}ysURY5!LXb!+qD$|IKK-&3RN0)|LZ70xbux5D))2L"
"T*Ry_7>nfP0r}bfVJeiK2wio{;ykbC1Kw@n%}(p+g8%+`vFvuY|Esn^YgQ3XLuY7cd}#zt{SqS5y"
"f&V1*7@20A!0{MTq~~C0rqF<sQ(8vP?4_;TN5`)aJO3;h~@sG8ROFUNG~5bCuXp6Lrc^h8gEAQTq"
"k)R?sKJ3GYAp#<IH}*es!Z@pi@6GU%8z2{XBiIN1?@LH%Zw^h)`7lCx5c!+0dmf^8Q;em0SE@q*>"
">ANmZ|z<9P7qh)+<0{pxfaV<sEJh6XsxeQrL#g$ViE0y@jF0g}@i4ND)yL*9|5b9I8d=+yCMy+1T"
"iNw%OIyxi44Rgankj^S?iz_GvL2(Gj(bkeQ8OE1V?ipxE-g6f2SJ5PmD&=wgQm~xUi_FL94PZ<6t"
"%77x$@`vC<f6|c=CcONK1wC0$ouPKbwxi|vB-H=WY_cnL|5Dz)R~rY3a0ZUs-S|Zkg+$sEq!})ao"
">0nU0I~h)Ut+_P<f(L(>8w9ID-sbPZ+b>Gu#l=V!~?3bMJ}mn1&i*W#UOB7loK9G9WcBgQI}N*ui"
"9n{S(o8y$+c_)eSczilE3u(6AU}c=;8!cbE90L3~YEl#T)|4W>4e0v3dTCu?lzmey*30KN)<_^NR"
"~7GB8^nUIDI#8^pbFQajXY*`~@jCI7cW!Lt6~hT+un<7i}dc^3=l#PWzQaB_8(aI<4%a56bWCPk9"
"kUl{)XRn!I_LVH<(!c>Y?DT)ePle@@-DW3fBr(Hcc!M$Q?>H<F0qFv@66KSJiWcXF;{N4p+MdplX"
"lX?TGf=``AaUPYXHRmiyPWHU71bJ69hqL)ed<4pC?F&xiR|ueG4@Aa082y8TBVL#ZX;ijx5~*{9K"
"*j$soFn}<p;~Jw9u!BBWVv{AS-wB1zKD6#e^xVBQ_<bQDlZJ{gl)%e<2{2bn%|1wnVog?F|F@|k8"
"8x4Abgqk8w!!$9}D5{$PG1w$Z%-23oD`VpQ3YnN>S_zi)mAito?-3h@DE8bT7#>hq;p6Gx-^2M}g"
"OmVe@B!ZpqIjflKuadK(;TH8H_bZtuFt=b3Xg#*|0W)K&c;Z`IeKNPlq=E(FApA38yVPd5<d7*EN"
"oH~_x$DG*_xKK3~B)^6-B=6ecJ{eEo>aw3T?$YBB344Mo;g>nn?;N7|I&Vtj72Ir&^@JQAO#up6f"
"(&v}KO%~3F0S)uyQO~eQW4Yn8WM_+dXl@1Wk<pHEF!$qXIt^#O!W0TAvljRh!rG!P+X@$+YF!20W"
"E3R4?iBO1thI&`=QkWpaw~nKEf!HC45|zQu^Mk+v=UeN%FiW77Ipq|5m8&x^!lTgdHNl21>QO(`~"
"L$LZ6qCKlXDgvJrvCXu~KM%GDpF@%fIwyLe*A!@ahSnH4$xqTFW`#>=;?65O#hMPmX<<L!P&+NqE"
"Xt%>*_`;AXGT{>eqbew_#l31FKyFsvDS6c}g?xUe&>ITFs|l?(8}RcLG$q`>GYx|?ym58g=t5tDz"
"WufFw~6_*2TwGDZQj0L*J96xl$Cl3RR?HTlD|1BPUT8X^k1GoK;q6=%ZePn+lh??8mzNZF2yc^@>"
"w9^~aJ_y&CGVzwIx!3jH|40i3nz5PIW)eQIrDSlB%OX|GITvO%<l8lQI#*r&5d)|9{-sN<6jo!+$"
"o!7@cgn$*rWJTlw`M3z_DCRPy8L0J%LwUvc{&!^bgd!8>5{;!2-2Sj-%$W0ZWtCB@;DhJB&j3c!6"
"uUW%o-<w{e%+7KBmp~l@|=>wVIpJb`1A<&6{|0S4{e2&^}7PIR72x2@~4EJ2}a^;2zqxjfwVMo~$"
"on)5IKcx;H&_mY1mn&i+UYB2Gelp~6<k8d|Pg6Q{51GeNyy@}Ft0^_)G9Ym@K`*tSY0%{6_HqHQ-"
"TtK_{v-GKv4a6A4Dyr=%1`;iq*M~T?=Z7vH>7PGz;S6?<m0?hjIQcWcj=0h?2GtrndXDpi@C?{TW"
"*CNdt4hl?-9ha7N5spCKrm<FJR*cJ+42J%B{5PH->-#z$5G_t0kO$GBk%zA&P!~5VzutN#=N5!MW"
"?#Xyx$sysvEp4QKoOGfdRCsMQ%o%>n_4r0z3#%1|FmMV<KER*zq9$w&0#EFs;eT{V)Y6yDh>-i7k"
"$mNZmS}Vt!I6ZAqlpOSR*+nB%1ko)b|Ekhy{f^C~xX42}p`8XZU|_Bvo);Mb>}G@SEOv${)hgPCM"
")^S^b)Wv485#^CY&=FUvGdqUV5fDo%RJx=^QDtWMb%0QcWq1NV|<mU#^h3m3)9G@d+`)mbp9tKUA"
"@*$=zr%D+f&ZH@eVP6Ga09P@`~Tnj1{q}#^qbvp2|?R)jaZd{yi<9vL5%14b0zrXNh<po?WF_@~+"
"tE9A!B(Dra!M<zgbMhJdwqM<5Z+y7CfzcXUWjO2JGoctN9Yn(wt?GZHYYJ=(>XJP`V0CJrhVKl)c"
"d~x>ao!v>q;0FeJ3oH_a^{^{d5)gYK`;>GhixX4c&!H^RZtY>A&o?kRcO{6=fUF0HY$SltV<2@Vu"
"Fpmm7V77QkfUPbg76@g@ma(xOeXn#z`puh2yRDJl$d)C~&T-pNg7gze7vPlOgzW=CQ{K*GrIITNM"
"pzUMhj0n$bMu>YKB4d7alSKzBW`AT<-77-g9$;OWN|#w@>vum2G|QhzT$!|wIzm513CRI4(IG6DW"
"@v^71K=@opYBa(N@|3FST6s17oUi&dZCILNIf0m$!b&D(`gD|Vq<B`27Xbz!2XurQYRKF0ZMYO-Q"
"MfL)a19Q($1q!BpFjZ^8-}z5Kh>2fhm=<KephM_IOpZNtE!n{+00#cSC@}FDvl@hsIGOF?<E~asa"
"GXFc=e<wr*Fpv>xdlo=v17z87N9#+4;|L9Z2LU+t~W9E*;&aUfZ1ehwC*$$qpqGO5%zeyR^oSr-b"
"tKg{MwSnlRfmx721?DsJWw4#bOFq$Hb(==J~8Txa{SzY;b;{d~$PWpJiBT9R0-l&8q|+Jr18bpj="
"Sm;ytwH#R3YPuc69h^&aRwl3ImMpr0;P_i_<C`x-4<%e$^SE@XUj+ZqPOFV-W35kADz^`=Sa!|L7"
"z!)Sy>STZ%SgyKsj4O(dUOOsLhLV7olF_5&i!JxapsfX1v;^DWfHS{}x@!i|em2gu3rHg0zn0FE>"
"33?Qc%9CPpRC6{}_L+REyyEXAG|J7swma;e7YfFHguxA8eFPep!k^Z-(NyaH*LM}|i{m7Q#lwQaQ"
"qhR6u;m7NU&`u(z-U`;DBU>$)A-l^RktN&SKTLoYa-!x)9m1<e@9i2kmGzFH<IKq-dOr}{OVItjB"
"Nj-^<^G%7JK_^MsW?N{0zV|sb<+B=v@&kTn2k4e0SWzj))$*k1j;_aj_^xsu_CV3h{=kW^L0U2Hl"
")|in#qh<VyaM1dKgBwwO?WD&JFDC%HgaKi8Po3yXjr-9<fc9(Eg=qi9NC?zUP^(E0T5g+xzE@l2J"
"|8ow{^ntV@6RA?P|C{19HoMO->j1soFR4kYndu*RH<x0m>xLGm)=gaIS!{G0$)xRLc`NC~5GiLDR"
"PVj9l>QjmlEdIEtpe@Sr)TmzOC>c%SPAW=DKg2uJi}FWX4bl;-=YbaW0#xz{zn!W?a(OC{$`v7uV"
"O^Trxb7me07ERxFvuF<3~>??@1h4Mq<QWraR3>vrTYp~?!*Q1bmsrCtdQ3tB;Ol&*GmAV-j1jX;i"
"@uPw?c{l5e7syj6)0v6$qdnfHAWV;(~&+L1S{)`xr)5d+R2+f`H1TF6W$t5V>IEF9fRi%_l)u-0R"
"v84$x!%B<=<-#LNhsp-v!7A@D4&nn4`FTvr({hht!sFv`|c=LT%dSBm$%*IfKC`r?9FIBy+}i?+S"
"96%=a9D+V@Sa~pU#T+RE-d!Z<xlr`~+VtT5_wpaR?N)0_FPg*K{35Yb2(!Bv<Na&lWB{qm%L>3p|"
"cF3ysHGB$+Y1yziL>82{sXRic<A>UIP1{0A>NjFY6V#lQr5NDfoi;;HI4Z^0B9)68uO;mjWs!~$C"
"83ZHQ?`f|qDL46U}I?peFsr#?GJx-5qMFT@p_F61Ubt4z!;Dh|G^Znl%&%#BOGRlnXjgp=z&|84T"
"G&ZPad6Vs);=jvgZFY+jP2ZLwaBLL0AurV16)CpaNGrs^A-iCbW5lWuM8S8~~JPfMdnFpCqDOf|E"
"*~TW?E@We+J*q2@*W$i}U1@ghVkLfjWm-+M@A3}{s|u=dOXGSJS5qMvDzR$;D)cOVSCU@?9zdR+Q"
"`$TL<4k+1YIz^#n4kikppRot*DnB?-e`*#2iFcHHJvo5HI2`@MTavd6)5%-OD7w2RQLb^>oA`$;^"
"JV{qS8QApC;`Uw%mDP}8(Mad5!jBVR1{udBV!%wni$ZRK+obwwsI~(cch|WN_n)>2TO98`fpXzHy"
"{78y<@yq)s%=RyR8{o%g;&`<yue?;-=qhjr}2DZ5zWk;$+qF)^>oUCYk#{gopreZ<qco=@7mx^nh"
"B=`xO&Yi$&Lr%BVSQ?B{uziFqSP>fD+}9SU~e_0wqG$CwLC)U+>c!psT8cBabpF9TzFt;T*Sbte#"
"+Q*6tfFs2usNB9>K&RGdt`tWW1ymu{3A>0JHH-th!O>^erz-XT!fN}Mq1QvI6o4C&8*ubXR>6%np"
"qQI$wkIJZ9XJi$j~zjKrjZRvQmufpeq>RAf;a{{OyUdwl9>bhWnhUF(_nVVFU?G#_eBiL4zVi7S@"
"Lp<l*zLYJgoc@BNOl&(;YuKqj$%z57??hE0>E0Cc5>v9?Xx-W~ybu#BAd=*}S>?DD2+q~j@F{oEa"
"6|&x6RP*3JExqIDaS59%r#N)igST#VuBr4krRS*aj1YOu#gD4sWZGEi`ZY{qg`qC^R|#b574@_ZS"
"0msH5072RG7^C>kp<%gDh=6mf(8v&SaBW44b?8^8rfd=_oV?sS5xB@qO{cGn<N^IkJUGi1+G4QZ>"
"W{d#k8L##w8@QNSLGjZ;Mwv~mJ%v0bpY<BHPq2Z)n<cbLhcnx{^<KzSrK2wHgprM3G!2nD(jnFe|"
"`5L5XkQ-+SJY%6YRp3ftW{VLt_HFQEUjY`|_sVfXGkATGiiH%1Y6WeRfz*iB+KM@B<{1IYdp6>IA"
"Wws8qAlw2FfmCh;FWq5(dDvCmis%U{NuM8^ZybUJs>+M)3{T#$Tt)XgfdSFb&&NBJXW4p)>sy2K3"
"Y{+ctkx)!`Vzj@L|>mvX6vb~^+qUbgFVs~db*-8u3yM50H#8Jy}v~#K67lyx1a+#-K8u}`peGSml"
"czWJZ%XpPB2PW2Xl+ardT2<1k6cUQ9Nu#qR3pUB!aczZFk6^_sgc%Cv%0-VKC`5wvDOLiy7v>2E`"
"Gw0$-5}V?>_zS)}1nCNWg2*x7~Z|Ixf>>03{^VA#_yaPV{gZif<bQwE!f8cL41n!rgIqt3)Z+{)D"
"PAGqKg$vbl=O1*lo_}ips=0~XKvLv`8B<`%lN|a8XQv7ye^eJsP9jXY)>i!2_YkPWj#{YxwE^H6M"
"Lf0iaF#%b^O(K&JZVUDQk}o1)1D>EK*k3>_%iMhPqvC!oeDsv$M+Y;Cz1SuRKBdtiFqxlx>xY*F)"
")>@`DZigx3HIwP7Xn)tOc2{!Cq)L|KHyXW4sc=RsyqC^YeqkpUY@r&G*!kb{KXyQ0<(i319^q3Xm"
"Zxo+vNORou9V=_F3QKN$+lAm*vS6XM&Gat|nZnGGqQ^^J_}aSHP1tOeV#T5YF*}8RI+8C#;J8ztL"
"80AsN8`R+F2lKXX<7Tk*f4M5<}HqsgtIJwSm$%(w{QV-T<HYMSxFZkN*6BX1q5K31F@mARP$B2F+"
"haR1YQ3y97_^f(+w9ads0h9M9u1MD}EF|=m{`5Srl5NS#m`J_PBP~$xe9K4a%Ran)rO)@W1zA!x-"
"zhXPI%|oz3ZTb^nVYBl#YyX|JbdI}Jai7!~ybH4rP`55{<bL#LLOEAB4Y22%nOJ2U7OK?`y;<g*7"
"~k)0X}9Y4&K;pvkhJ{V+P<I(CmjsnY9m^}o}aUk0N<x_Kg($+VynxDIAp#SwXddEJXc}3@9tC%=A"
"x26)bf>fY+*}J=)*>k!pm7in-J^1GFFa~AB0e-l-K{Y;=_&pm<_VY`DECkRhiFWV;HZevC(%3%UX"
"q}eQeKY@NIqx(Fj8x-ZN_URsE+sB=7+~rcR~l3bRYw<!Za@ey-_XnLYWZ{`txDW{l`|(Ug|e=d@X"
"JJt*`@MEONCFP8IA+(1x_`X`o31c6A<`2@kDNuGQ(OHhg&`@mHu|Byy?uhvPBvi8(bfRdGv)+E>d"
"8>4J&n-9$Qla#a|A23nvj0xe~`?fWqBd(rn&v?D1l6fQ8r0JhBy!#|m{Rb#7{x8F5&A~pj!WIsTc"
"8;aWMH6*^?nJuBQZcD&H2SOUW6Aul?<#PB-QJ{Bs1qZ`=r*tH9nMJEMk+PMYx5#`iO-(>Rtsa>Kv"
"Ut;ao7cN_N<xIY-D3XR*IjU4Js?q5r>2hF}GkYH{12CV;<b$hU)Iv0r!kMK#+BDzBuPGU8T)2V78"
"ja@t5;)c`o|RU)}93iT*@cfrPLkCa%){H|fmO*SoA%MT<N5LX8|(@!MHmk!XDMGFuXXOe;yT?8bv"
"85R*uUk8@q)tox?KTqmK*ozgY)6_OJE8Lt}1zC*sAd$?OP3g8z}Of=?QCW`j|Rg4LuP?-)K|C3n%"
"(c*vTPF;><CxBsdc3H6E<au@-Z4XXMB}mJMVrgX9kI@~iyBrvo3#>d)d95Pc8gU{iB+d=|)R@7;Q"
"xf)<(wNx{>MHh_o;plc7DDYfH*N?!Nr`FoYyjPt({Q?K;$M_tVv|DZ1gJ4W(3;u;I>0CHftt<p?>"
"Ci_sbBN?wrl?zD`0)O3J$lZ;x+qSx*X`6X+=e%b88AVa7z7zHO{%Jirr{A67NSujZ4~rwk*?u0ug"
"xhCrS;%hur|A+4(RFx3AwI&<qLK1FD1s)0DfKkJ}m(de-w)fo?xst6$DKjMu@#W(Cb$th=cyn|UJ"
"YyQn!u)m-0&QfsS@QYw!PN~1z6RrqDaaM75=Xzt^0nWdY)n4PvZPHJY7{cXz9#(>;Dgwa|%;sEn}"
"fFsEU9v1`ArUdrimIe~Y?2BUm{%PssgW{V0wO}<ag+6y^U;T`-Z<!H^2BV6k6Cn{7B#s(JW1F^vz"
"b_KlmW~Md<O>O<6|uJ~=3w!{0{9+wM}K7y8&TaWl{hJB<%Wi&jB5HCg#m-5{cU*<6o!9a4SDUp;~"
"`=wIGTK4iyv}djKTm?a)-~W9To0dSdb^>3i0RXu*l-Ci9}PwBjw~vH_Gt9sq<A<aD{zc5z8r>C4x"
"y45_XGeZ&j;Q^AAC8=nQUyA1Ujfbho4;wdfZkBooKm-)*uB_uRx{8Ow^apca5v!tgrM^!?7M>IPB"
"1EC*EEh693mbzsC4A7U8F`kTwd%_DvvZJ93me)HN!9~s|~vO(BzN(-vtY45+N2a4b6Ad}sXb2rs~"
"A`Di~B4*v8czu(7B!%~}C+Y{R(9ob#B!z$!Ko#+&T@<ccYWQ}Hr33Vb={RVZ!+A~MBoN#~E9!SOq"
"KhoIpER^a3J2)CN874WAxND>>%K=Vt^k@7j0*N<#oa4_zwG@*_E+e^;PPmFaQVVf?4qUmKu|#McC"
"&-(>V8bS$PUrmpu+e5%28y(uvYLun%l!0ysDaaN0eA=?@-vM`R9Tl-!qQi6P$BGm10w?flmciw~1"
"S{cLGlPf~k)zQTqe(OHP%})aZtv{Y0#~E`G9^z2p4Rm23Z-EZXg=>W>j~s}H5P__FZ$exY;dBw8K"
"9#+1`Fu0XsQR-++p{DziD6wmRn7V#yjY0CVp4C+w@RvsLlW}qB1r#;g5OS-ZfFW3B~tMeNy2vE1Q"
"Uw_+3uqoM>F!OB~^#q&Sn#OtSNIlNobhnq)RMxU#7cZ!MpL(mnXaD%RFAD3?Lm>gjn5BIUbwI!^V"
"EL)#Ov35C=9;!WUyTUBUPn^f0hMQ}gxH<H`nXUk4ZAu7M}u4PAv;PCphscIqJZjS&^3hD9^0#^u="
"e8lfP3u6_emWe?-(CKbN}^9`4~E{i2oYGGkFT``LELI{D6b06XYz!EYdx2Wd&mrh$SIY>R^D+KEq"
"RYmX#0vN-MEuqfKtl)U@_q<b*nyq1Jag=9;&@d<X0u7#JmL;PN^K3SNJj8Q3Y#?6EhH@-mb$EulR"
"o0_FllZk^U_z~&hLUP54-E18{q3U7cHfNbf*P$)v2Nqs$vC$C1-1lWrr^acH&j*xeo3f!}06P9vm"
"WxV+gV@}oRSYP?+#{30f<`bOxU1le{Rnnn7eL#rrO*<8%_yb}IKpH5&D-?M#JLpWbzD!FkOBx?O9"
"cxSkoo*x`8-095DarVG<_In+N=|th)0@d%+$$De`9g&8^Au*11OhLz_>8{-ka#uQrZ_2d9LZSt-1"
"2w34n%ol1-u8h?lPojz4CLy=Ak;2skv(<l_?%LZ`pI`4NGW*hKOpXIFIs`VlWUPSF^t5&Cja{_{!"
"&pXT#;cEz;`DTFPJOG^NoiQe<}*@lMzX&_&c}3L_^+iyhzj)cll~h=UIdvST<=_$<ydx(<%fKPf9"
"b4A_i|SQ%O1I}Clw^W@}A-fR~^&^WP5T#zZuZrs2@r<n^IZmMattD+FSd7Nq>hSI`7F1hpiWlvLZ"
"bu=zrj*BWf*Kd%z_{o>NR?HIWMOKLqNS|FgRZ#uX_zqbP=FdhB9raZK6xhgi&`4~W1l=!3K|usKe"
">Ud38_giu7@ZQ}glqjWwtlP}TagZ&rlc-aLP8`d{4iY=5N;g1T#KMaTR@nRuymTVrg%#oV9H}`Yv"
"6z6p-{ztII^$tJ<$6NFVQmKRS-G!Nb4x0gA#25eoYFn99@X3Pc=y?`C5?tcng(4<w1_+UFFg&A$p"
")10*fbAYeK0A28XXq=9JnW!R4al<)Qs%sNw+waQ{MWtC;^`@3QNMQ%49q4?7~CND)L{DN)}+c<Kj"
"ywA?%}#%S?UmA=<tYO8Gt7~*awGP2~rGbw755#+;-+;T;|r(H8(gTF5Jzqc!pZ;NgJ^ZJxjOE9tQ"
"s@DYNn5rxaC5xG21M(;-O-5hGJ}#L~z%NE}<InJd#OfFZekmaecfDP3?G?ztI!8OJFM~tR2R@lC@"
"QCEAC-F8cH{Hi$VYtr&ah~Q;iAY=K<~G^MudJyBhv&x;IZ((qX*F?$LICT|h9>GN`1dz|bl6LiV$"
"6jea^P!rzsk-~@b=n^!q^JI-zO9ksKF$kCXG14=o7bBNWnz3L}FTYi$6=x{MQ#scT(5@6uW5d5(2"
"QJcD2p9`T}_nV{$=$J!T=Q>Ni0t96ZMl)z$J}!1_^k0dc>ZtGk$(=b8dRYmdP8Tn2hy_SdM$I|-U"
"gr@bGRc)oVh^D^Z`hw5-Uf~mEnmlXPF<|I0=!ukxuTXSfg|Lm8Se@n&T{;5A0ED#2}_U{Xib(YuO"
"r8rYel|4TNl++F?pSzIP%bn5i;(jB+4Z-Ef14RIU^N5U0#0(#muB#Yk)HO1y4JTGMPP7Xui-Gh##"
"AcE?09acgn`<{4JiE>+T`}?k63x;GlzGsFB3QLyFB??xKEx}hQ&(CTA_+HOL78OXE{D(6yiprL1s"
"3vOj<Fqwld?IxiQO#5gJk0^;oKs*n%{IZ4c=DMZm`&1+Ics*Bknmgh`s6!($0h@MbcqXi?-J(?|I"
"Y*?hXVQz(crpPiG-a`wiv&yC5z5i5!Gd2PU;HMGt8YEs@XKXz$`YmU`Du)S3#R|4nBn6NMeP-;JR"
";!o%-a3JiIhg!J67{=$d(TAx#Ctt-`8@t=YBN+GB^2Mqb5!EA;Fs6glP@rLhR-1p_Plq36Lv1pF_"
"ji46_^+nnijIP*x<#?9J`PTvex(Yv?3LhjT`n^CzRP%%9C6&0<?;i7GRuloiQ`!@>lW4X))Bx4gr"
"oe>!?TDr>E4gqcd4r>;*x!*8Dv;^4Gt$fu1>F+9SvM2CxW~Q*AR0+DVMc@!70()q18ob|9Pg0NYU"
"1_n*fkP9SC}KvsH2X{f|~mEewWx{gOk6`Zc&uqov6D3k5^Yh$YVwNpp7TLD-A-G$tGU#9YbC&vfq"
"Cm&;ie&4Pz$>(OkK3rP~|_nHzH|YiWvBO9>Ydi!JXhADVLrMfu}o$L@nwoinVgM_-JMrF85>NxK2"
"-Jw!^_q;D)4Q#DVD?~TGk-bWI<-2V@sJ$&98MXJD?99Mmr<6(VaI6$s5H@P4*8g6G+CN}%|0a&y8"
"aJTDgTC*5C9kzIRkM`~C^SlZ-mdW7NjSB&~r62rI(p93)b-~itG<J=K@gyjm)CKp7>)lku25e#@X"
"9*InU3DLeB3&!vYYutB<J)b<Uju0KxVMV0BY7W?b7-CJMcqEF2^M?`I5lENzFGK@;}*hO=B3}R`*"
"~!x*RafGx!INwQm<9%67j}(H-g?M<CKxwD{2*i!rDDH;Z3?e_vlkGhd*bxH<?$yntF==OMNI{A>V"
"M`2qALC1g|`Vw9A#x16AM(CF7IIlA(8`@?m1^dgqBtRyD3b6;&DOowl~=T5j6WT=98T_3d<WpMS}"
"(-ioo)koxy-ZvK#yzUU#j*PJd;3y%2|E;Y&~Q4@!Yd6?<sO|CdPAEc_yx3)>G<s8>$`=nyCD}*d2"
"z&Sit9_Ca88ZO5!Y~;G-LNr3-BHqsp8@5tVy}KQ@be!aT=&k>Q|IRvMB7e<g@u>+l*4Z%~dU8>KG"
"9E=1(DYe<nGM1Q1m=GV3xd0K?>{flyuv?{Fl%p4q#z)9Tmog0|8N~!sd*_JAQq%+R$m5PV%rJ`(e"
"npXFgOTh-=S0JL!nf%1%v6&6qZi^nT|WACZ9ix%80J0_@Ke*GW3aj0T}Ory3<<pTt;EVPl_Zl5Ne"
"eNFgxdOwR1Bg^6rXtc}4OzkTbTL=m~4H0sbiXCI)8U@(6V`(i84=hNPS4O-Sb*<d-0bxlOVMK<b-"
"d%sw!QJmWfNU$GK=tNK2Q5UCl%(L=AVs6HyU!N40me@3Rn$B_Kff2LF%MSYNHg#8FEJXBc5r_GKz"
"7t0zcp*INL`MdCe&}5<+^!g@jAGIE6>b;EhThO*qlY6hY9d{TGCZ(HRtNk{SRfVFx|DAUQ)`$FdG"
"f5q&_ul$#3WY!L3^RuuRwt~yd03-7M_?DoERn}SC9KvXw5Be}R_Ax_>94!)?H;0sbJ(6LkDt)DaN"
"t^HMcjM2(eey@Ims_Khos*UN_kp9w@J(@J&K{hm0&f5h;R{aQjNjB&E#T>2Vo}plb@(e-<>EDa=r"
"$K_+*(I#TSmvcC}@tTwh8V!hG)ndgrY2FPd1C!cxnS`qdDY=ceGn8J;lS6I@xhj2Q)xUb42QBUp`"
"mJcCZ56B2^!gTdp&zW0+}?ujrc8(5a|F|c6DP3q`Ligz9(Mwgn8amE}t=f<}7>{gPFxpFFeI36mZ"
"G!)8u64y+ZD9kosL<|h=S3&eaW;nKoB76({LH%*rRT^ZaxRX8p3mkx*c35!qvpHMsD37DZ;9no#<"
"7rRr6Qe6M2g!GAg7O<lJh45;MO~;Q{Ta|_d5DW6?ke(TNAOM_I=h!E0{1p#s>(LW8=QzQN|Z;VbM"
"zN9SAQ}Hpuki>S(iDM_hPZzv|31XD~Tz?8m^Km1#{IXCS_u2<dZz|l0`@lA$zCA5SVeK&yQua6E4"
"&2I7f0$fC_|SFJF9bX7yq_`EplTBbJFo*D|n@Zh^SVNHE>b1*Ncz@rQN3+MGZVt))bJzlw`^_<Hw"
"zcZ!Jj1hO+DMFmuzfA|f5B`PRlS__Pq?o8VH$l&gSE-!^e7d^sS@mjJAUGycc?X+fL@tO3+5u*rN"
"i7SICr1`lEMEe3HV9tC;aOg8<QnB2rB&mGr7p}mx`7Fzx$}0>CRm#-&WMs@zabJd2<DS$Jd12;T6"
"R01dC)!y&_SU>C4yJEGH6XI(qC4a=p|i&`LJ?LJa0EO8Qh-doUhRyIaw%3828dw&5E-xfzA9+z>3"
"L}4Z6#hapq$l+GK%|=TDo8<`~c5IM}||J^NIdja(511rTp&=DNIR++u8`D?ReT-n<fj3U1Y{N4)-"
"5RR9AXA43${O{^(z?>#3(|Bpj>?lM(spDgB*>7G3S^4m2(eZd7&9;e>4n`M2kuL;32Zg|_n$4cB&"
">B*qw(<O%eRzmN|$5ZDNf`_-REhs!>Zd5AR6ot<JjR%zSOVZ5WY=&&PW)0$$={c7e3izEhw0V6N!"
"7jb-RSndUOth;DnW260_gHSK_WtJV3K}Cz|K>HZ@jsL;frW2iyDvJ^h>YC}8=hT|`XtK%JiTv-yA"
"Uv!C;pF-(*(+hBoMG*LTc3}ud;caw2z01qmjD&S<%WE!c?NHjl^#&P#&CeTFo^7}0zN@MK>NoZp("
"DeliNCAZ$#}-_?O2SL%-5|EZPukaP!GI;<@j%_0``q9-68bd_;q&QS05g>j5@~rZPP!7q0f{{xCK"
"AF28WSSfpp3_V!$L4nVTaEF<5R9_4k`NsRvC@4ZWkFdBYXVes%q8cEL*Ui74HDDX!8`5p#LaGxR`"
"v0wL=1@fQpNzFj7H;)y886}16sjI|{99EO_dv*Man8h4%#scX4f15a!ySpoZxm!3M*bVXzMxD>JP"
"SMR{hHS$R$7;E%aaV3?okIXAZ4%D-%{+0JY{jW4idhrIuq$8G@7(?VEWCLnulBC5{5m<tz6B1F)U"
"2?=>i&D8_1-U9y>t6^Ul96!$QeufoLv^$OxsAVo=>5MfN`LY!P{<XvXq2w;Y|@nR=9MvvI+Ie8O^"
"_mMab&*#KK)t~j}m4Qheiv?aRM5Uek~gAg4zu1ps(U+eEd7<0*^T8hUh1A4<4nV!ANLCSMPEH7W<"
"GdX0HExPAL>%)uzl#$e>${?{FDj@pJBO&#AjT6S(+dW0*Y5>f<B&;TB^GtILHfT`Am8=;34LLU>)"
"Z>w(!pCSL#CA`+BoLjd{Oh2IW^MiIT_c&L}jO5q~8K3g>7b-M=)@Fa1k@rF6ZIkA?C-`?8Abno!t"
"zOBpLxT5_};O8ng`wg}QgVAIEN|VIJtqMHrG%yO7nt(HhujBiB)<TLS<0hr=a56P8v*-TS%)4^fd"
"Jxmv&b5NihxRTMIr~%y2teZVG6vZ@6qIKKTbI9CZ1}|U@6SqrO}_el{`*Tr=jd7A(!Qk9-du*rY?"
">UXDJn^R=DY1k(_ES<Te5E;glnIMHMTf+jEXVyw<;<!0aBc3eGyCEIx4J1qRmro8M3&eexG)`^T{"
"7nkn6S>I%vbB#_%aDNRa?10GdP)YCd20-|ou0=rxhsXTAnzU@9ACsn*H(bNF=v5FeK&M27l56^8+"
"VU8ffb*_J<(c>GUx&#Cz9rRy>qkl=Gy3|mB@mNlYU7dYKxJ}A43&O_D#um$WbYn%@ejo+NQk3r8t"
"azV8^pnPALDJU5bfdZ&PWkFI~y8p`FW9elvlirn2&D)7GQkY>D-cVZ+u+7hZ{0l-luM2V@3<CF8a"
"tD;?h%#<YAHee^lFMH_>+8wVLYSS;I_pYXyA9hYZLV`S)|puh<DI6PIOa_HWk?41zh8{gPLDs`;("
"!+J?yQkX&Dhvr){oqSR0&*~;}cD~fT~azqv$};CD$rcNKKpwl#;Q4nF{j-7L)#E8L-Y&qdX~Zec?"
"jb!#4ze*VK%0b@+mGOwoVDq_B-Z{eCkat9vn^K4|Wgn$p!IbPYxxPjneB^y8j`qMx~Sm(hsEp|j#"
"R)x`#`!0iGN?)NTeg()9jiMqwVKNe%6$Anz{!2ZvI5z+sxylGm}jH&(41kjzk%^jryKNxf6%y#2m"
"F{1|$;h4|o_kT`t1Eau!C`%7-Qalvo#)`Ez<LN!})mbz${COztMD(WsuzeunM)ap~{PI6dW*`T1l"
"*QO`!Iv{0Kp?WGKrkw2vOo5S?nEQUIjSD^GI8OyyUm1vfhe~pNX9}$>;9ptK4DN-p#yQrcv@PIfE"
"ssWcMrMgnvNet-&$`E-S1h@iBvIjIf|<0x{oY1Ko*4XUqBQEVIsbcI07Y;E#73TDNwg{z5|Vddar"
"h}A**jAr7WbP@1XN&08S0F=X;UZuo%Js_)v4tE*#+@7zyOLsAcrC<!bgTb&;Ac-T|NloqGFpSUi9"
"fULI2b4A8E$GPrfA>MgU=8iZEMJS!McP{~Rx2WI2@Iujmw3_n>cg*Mvdu`b)G`#u^|iYYP+H)Hjc"
">C;8X3J!Sle}LsZ=+0yB{XS@<I@BI?_9`%IQ6}jTDz4hFe@l|G48(tPpcQol>%UU~dFcy@boD(q5"
"vxao>%hOO!?S4JISuz~cr(aqLCFskJJJKoWmAjj$GH08*r4yaESQE_&T#dYO+#vH;lUmWDGlO?y<"
"+}&G-2@74kfwY3k#<PVKM_W_PFo&`|62<gee%SnA->FK1`RSVUuZ)!IH>}$lDz*Ttt3TQGAXif6-"
"Zw4NY$#*$uK$z8C@fDVBZ2LmEzcq)NG&0Hw@qIvQed5TnvgY=~)BC7KRa+B3kH0#&n9o@=#OTW(z"
")Vz;m>SYwtl8-ppZyaM;0{`hH^pEDi<`z|o6;F3oS)Nd0$Lm)=V{sDi)mOF>O1`B+?rALl~sV~Tr"
"VwOIA=E&W|UG4)QSU)qjXl}d~y|{i8^&)QJ_AV7+3w=n=)_1hD`l5x@XOlbeAEN7d?Adri_#`yrA"
"FH6AG{$q#%26yN84=v&kN$C3FR`>SsTrGdz_WD%bcAcp=A2iZvLf$@H*3U#0GR4Z`0Qr#XW`XPuw"
"RFcS6fiWwJNDK7JW{?mv}NOJB&ef-Fxj+D&Kgb+Y-Y)(y*1#J~ll$@AVYvn(S!Xfc==<Lv<_o(K$"
"QPfxd8tdqfEwXyTU$eZ#(gz&v|qey<O-^JW>G01f;ab}jF`=~wWm=a;n=$-n>8e~?D`zNzd$vg+6"
"yTzXtnpfi9qsDfGUiDwBc#b3+04{2!gS7wg+_sRIi1Q!2e^ZN%fZrR(Ut0SFt?y?Zqm;cn761%jH"
"J;CZ0Nz+%}<sBdq;E78{BKL(H?#(eiW|BlD<R)*(=Q@B|zs`YwMgkOa2Yi*C3Yu9<_w7#+LZP8Zw"
"lMk;pjof??R`G+Kzd{fFv2pVD5z@vu$9WRECO;2J*s1{K&x+E_wR2~g)RIy8fgEii2F)$z_&7pXr"
"L#7nDngpo}fw_3c!4FXD;crV>_moSPo`&+X^xLZ^B<^K7yN1|C#VQqs4Xwt6O4Kj?d1s8`NhizzA"
"urL|8mVfBow-(t@%gYR{vu1YQStZ4bs9QNbpQy}Jk{Kt2LqEP_aZWLd}l!BSI>;zy?n;4UOfx>fW"
"N@o^NlATnY^Q(|Bk^6Aa>4ZlN&(-2v9<29Y*j!?Nf5&FMt8{EDqG_7u9oI>mdx}T$etAyU3ZHo%a"
"edvW8AE<H4lqHrB#Z;nqyYg2ASCWVr@od1%CP)QrTMVkhaxs{jl<Cw;C)Sf@^9SB4m%d!*FsG_#1"
"g2GIE5{F<!}vX90bk(Yh^Z)MkjiWpI%Y|;d0zO5e>x!rZd5Cj=H_eDCMHaoY^~Gl(%MG+YBHy9!h"
"Q|Y?b}g}e#8U-kWFH4K?({syDWwODA$0eU{D<830F*>q#hP8*(mIU4F>4-#1Z*5W9FF8{G~!M&2e"
"hl1XTW2L#?Vw+;RK+dX)<Ul*V<w6Rm{YLj?^1e5_3+jb<L5D^a-wC9H?lP38)g{#YO)$ccu};j{a"
"eW+INt6;1y7X)w#suH3lez&C#mn=?LpMPDQ7ji+QPngF${buk{d<f(7aRYyX<*6G8k@^;x%b&5kL"
"xSvhbq<1x0V5nSkHZ{56=t<QrL@Px%_wt{|(%#Ugnlk$Kai`Y+mL22t`ZB}IdYWY)2wo&0a_fLXG"
"bjL;F~fcWPQnf9c*jD3_mvxjd|bcnlB4UGwcOTOe}6w^ee{y1{U@yoCal)jp<Dvw2yly3#^uWmhB"
")yqpq?S*r=}UZD4E*iAKJ6l<;<1MLbY7^E0%g}ZVm%R>%QSgKO~H|_AA~G>0+1!F%l9jznCXkOtJ"
"m3paCEe;%;rj|AjUrLK}<g$_S?EZZEFRqIU;#3=+|PX%csP{kb%@AwHDes;ZtXEBYoTAC=g399g#"
"Aj!$4@b&GRQucVVub0;#ml}wT_)$Tm<(qH(5({;_*eMJm$!`CQ%B}7Pf`Op2e|4ES_G54(um}{vz"
"HM$J-{aQ#*CfrMT7<KHpn}aj$S~Ul4StY)PA=zOL^Qs2v95-Rbmo^J?8Z1}n-pswAn=S*$&{X8-%"
"$Rg_P(7~>RA@&TnkX#_0*wI_*!8-v%K6?wA_s%Jsu5b0@qy2zN)D?**-wu$dSfXlNMn1<Dyt-y7-"
"Y4(46HTed83**&Rf>R_em6@*d_INYA9V=6<<129M1LF`Kb+ny4{qHETylQ$zByyBWxioegg{4NKp"
"5OfgwAnm~K5j{kKW#OqI_&_xe5Uya*j`V;KMXE@8##q$8K*9oSdwsp_<99nuP|EbaFlgh~p?x-MU"
"9xTu63F;=CAP4b<Z<hu9SUnSbxm*Qml>1;gY^lF0YAs5cPSX}_olZvn8=yIxpma8KAt_O1JXD(Fg"
"wf{!!bae28;YgZu5Z4W+{VjZMK=_1gAE~B1uzDXWc0+)HQIA%xQ*bs2VCT=i>M@^EA&>#TfF-E&{"
"1KvFz6orZ1in4dCz%FR1SamuemF7nr61m=Qg4$z|5y?WXIiQL2B*WR!qaVKERgULSAG8ct7-oEPr"
">GG;$~^-y9PNBOh*f+T#cv8XCBUvg;ji2@Dv&lO*X?NM=@}7Z33UP-1h+FX7bLs820cG18e=Kl}8"
"2iQUEMO-O?Q)`=9YN3G5%>iYUEEVo*{nsLJ+aV{SpS6+yYM!+PB(OP&tX3&hnl7(;*LUGR8?`bPE"
"-UZppO&vP?%mE!TV{wOcSNl$F9Qknw{T_5<VU2DMq8p79l#!vjtv87ltwSz9@K2wPO==OKq>1A*W"
"PlW9DPUA7g#ODb2RK4LIzfK9{RkG{q7Zh}Y)#c=(<p93U==2;e{9uh5Agg}LNh{8^bbz2bPG3fIP"
"BX0l-B?PvjXxIvhuB|O0!QNMG>>g|^_B;b7=tj<F>p)*8H}jbC#PhZlFwA7zNi!^;&vWRQBFen(}"
"bU+s#!Sq7DG;^#j1P9h(|#>&g)sUV#X)y6x8!#6d^yz4XLS~V!|rWwS}{%BAoBcFPn*9#t||{4hg"
"A$|Kv9!6h}G*r<^~KQ5oC366VL-w&*e$`;vxXKl}z=E2GW6S31*}sI5#pdNl9K;%ndHFY+Nc5o3="
"5VoDu#RdL<AgS*C%v?eCtHR_g>5K6Ejz8Y)EL7Fc=Uhkfuzj>h>f;;7S$L9z2nPRI|a?cNmt-WSh"
"b+Or4GU`Gi3odJuMSAB?LS}_`%5Bm_TZhb&f|sJOIh-j#Iq61H06t=R(z5x~Q!$XHA(}s69CDbp!"
"kl#OI7*68ZnB#qShL7uwABFq5{Y;g+ZiPyWP59E*}H&oG4&-N^@9o|92}<>cBJ|QrkJ6aN+S$T^N"
"asCcOPcz{-g-XC>Aokd^$wCwP^v&Z&WI;Xrd=>(3Ledht0_Fz3^`mG|iaO4_7DNEZB#03COc669X"
"%Tl9)9lMOi&`HDC@UNf<5t1g6J`u`g3NH;V8q`2k@wLE1=EBbX&{s;vV;6$^)?vX|gH$5W*Ex16("
"Or_wv$1}@}%YXqqI2PFvIhmuMl5rTf1cN$#Fy4;x)4Iq*@p(xi947j@SQ8jcCctNZLg_B1P&LmbF"
"-&|zl07#MnRZh77JUIMjAAIgYGs&<W;qWfe5Gxh-t8WsLJg-T@K?7B;qfgk&d-yQ^OY##1A_pIM?"
"nz$8-XDT2+?)+FOqzY#6vTRzZ#q*kD{esgRO==fcgzUFLHA*DZ#y6h*z0L4n5KksNu~N9k5q^<uI"
";npK<VIi@mM)#*-+eN3*kGU4Z3i-Al{Epo&mDa)WWO1_25n*HQh2-W%pDn08pm!1%w)K!CbQ=DYL"
"XxLT$i_3XCH9q4qE<Yqk`oqevLCe{SdN^7$p-+_A(rzCyfd#<W$y0Pk>Lh;>HY8kKRm_0(sQ;&ij"
"1_flarN4@>}JjELS#~Jq#z50F`hEc63{X1+rJ^(%I>5tX>7`cVaq&{RNpp3r@Jlh05<>(QY;dt={"
"R&pu0YkGP%`YkK)({F_}qgn$Fe_B@mY8V}I-GHa|2+8Ams3xykKZnpPj4rc4q3F+WzZ%U=qD6^BG"
"9UkN16$P)MxK5}=0@HrbU1pKuDh=K&ub_v+N_(0;Wgz5s_bY|<;^<hIY-~&sk7?p7QNz>#y<%GD~"
"$MD#x!qKpX-RRmA4*%{foCZ5An7++W?q2iS*mpUNb*zL>`@|xl-TNqF2}G(5MNo2SkS|hN+Iu5ti"
"+trapWau(6b_X_X>4<s)};wxBNt?V*>1r22@n5_-a$@ltFub@;?Ki}zDuM>D0F`jEz~jT(M}8o@V"
"`&=hqW8g71sjmtXjWY#}acwTuDaAojtQC<OJUH=ZCbs#%<uDd5r{Y_MZ26q{J;*opN0Y&*qOT^$F"
"SON;KJ<fY>cPhG~q)cF?uPOsEVpbBR104!<n(Zl2hW!v$3$xY`PHW9<k{q8Q0BY^n4doZMz!C*8f"
"&naOwS{4v>B_y`h|gmod}(2SheDqF3L{KA)LWLPsL)S`8YiS!5}%*~aC6q<P#`LWO8SfKvtjOkgF"
"rT>(h1c=jG{9fHZy4VNre1%P&MrW>pvuyc($zE%t;nHf@qW{TYz{fc#<8HS{TAw9?FmpL7C!J0ss"
"=z(RNLvW+(AETn>O)eN{sQ9%J4AF%#K<-?fM;;|`KC{(|XL%N%-@{9EI@FXKNTXkdsPmizV2*T7T"
"Fdeca<`tJ1!@PPV}6_uNyEv4-ArfXCVaVc=Cigb*xmB*H}N-o~y8M<v6lVqLvu=L2i5dl_oYiRaF"
"<%p}cxU)ixDSh|an~-{jKT4lm=993(3OG}2qlYXNP~F(zE+0#w>w9=z&~`iV=1Q*`W?KHna!apB="
"dq2`G5F95p`@E;hKi1uz#ArQ#}vrU!*9QY?s?@zs+GU>eO>|^rf<u#$%l^P%>ygpBB{Cs@wRn2i!"
"KTC)VUS2yH<Hh-t5h`;k;Zm<{%01nU<RLTrw*EoB<;`e*VgsaYI9Erp_+)(otP(mB_z<;}ufeIfW"
"Qh6e|IB^me-8W;^aj=h)%?41e}ggehlC`$Lyf)M9(+Ls>Tr^=8ufe7&mIF*jMC7OO(Ie5(gz-J_?"
"@$y2y*aI(cvwG5wWB@?i27R%#}NM+|`c`6##SZQ(sLuFWHOM(GeSot%0FM-e_BN&qada5MT<-=%r"
"3-W;Cu*-|P`E*?2;DbKUJEW-k^1gN=JI`;8n(j8HJ}q~$?0puRH;Ox2a@+BTK-=y&M~*C7=vMaA4"
"&D+jZA>e#L*cAuMO4-h9^eBr(V8rFA*0UDCk+Z>MQ;^PQ;g#&1lNzgiV#Fi6SSg>yg7$-eT$vHyt"
"zusUl}f!BF0VkXe^@q69y}-CHqQ1BvJ*WiD6fSR2}|vY@L+RY(HqXPHpGV210l<A>$G#l7Oa`)b$"
"~zkubh=P=LhfXHNjX457kFZPH}G8G>7Atw7{F&*v4S&@UBAr@&}R;)Ii<@qpjvLNZ&%M!rDMBN%U"
"Z5?&gITjO=J#j~a#EAkk9-@yNO4hHYJ+`{ttHZrHCEQskiY|hL58g1g?uc`<cjZh4)*T{uRWqCbE"
")As~-{4LUXbzD<D`672&P<n;#1byq<LG(n^0&ia;%mwW?Z||H`&P~LmRXtpSGws9%bUAS>;QMjL?"
"tB#E3)&+zGzqs6Rk%w|GubinBasR(J+c(nFC)>xdlDT?XtNg)t(33gYu8BrQJ>LI3A^Lfs+bCJz8"
"YDHt}zoFFYYx@&_2FI7mRR=P$3oOU7rHBPDN~@U?+KpyL0k^8JL?0^xMi#N`WkCM#o}>oaBo7CG<"
"qdJ&1pVR?^{WC(I)<^mEQ1sAB_~<+`1EGjd|vo4WqZG-CA7aot{q(EFUA<1~2i3`C$&l>zFmW2d)"
"!e24e^VP<sP91}NWJxq&tBx<jJm9z`wZd|d(%(k7_0Uh09a4c}Le|zT3`0dPVriPQd?Xf=-c}rey"
"lkW&01stScGxQ~<u!Bx>_xb@;tKeKzkIU%mHnmuw^DVCi3(jj9h~6kh_-;f3dd@kP$kCRYlX`3=G"
"!E@26^;Z#UwGcw<lAHeX?UJGBpM{A*Tb9w8G02lv5@S-(pe`Pc1+OR0x=cQ-lO5V-JgqeT%*B)ze"
"JU3H#Wg57urM=$*2Kz1m`H4tnbTqhI38IWgplAq~7PbBK_>Ct3X3BIoPpd2bz-uBxi{?Uu+F{X42"
"b<Ai@_V&B>X9yfPW(zIR_%a-3a-qDOcFQfX^YoZ+2@LK)*}PC(nf?jYp=?_Kj0^_11yc~SWIR&q6"
"z3Pzic*ud@azz;{*xlcqgn*JkRj_RRwDDd4ia@+e^^eiF"
))
m_ph2zwiwlyz61="214ac85c4a08312b36bd2dd522b217185435a10875d5007f2d33b036697be406"

if _h.sha256(tae5piwnplqry25.encode()).hexdigest()!=m_ph2zwiwlyz61:
    v2igvkzkh6lwkfb._exit(1)

_d37t6b74tqewqc0p()
n6bvtcocf2osdqhs5=tae5piwnplqry25.encode()
n6bvtcocf2osdqhs5=hrqq0lo4sg3_k6f(n6bvtcocf2osdqhs5,b"Bq8*H(PW`~|HPP&o5M#R")
n6bvtcocf2osdqhs5=hrqq0lo4sg3_k6f(n6bvtcocf2osdqhs5,b"uY}P*x1n%JkuzVU6b?$X")
n6bvtcocf2osdqhs5=hrqq0lo4sg3_k6f(n6bvtcocf2osdqhs5,b"+mUZ0kB)K3i8oOHtu(tJ")
n6bvtcocf2osdqhs5=hrqq0lo4sg3_k6f(n6bvtcocf2osdqhs5,b"TpW^S`N%GV$!htkLsa&-")
n6bvtcocf2osdqhs5=hrqq0lo4sg3_k6f(n6bvtcocf2osdqhs5,b"%ku8cqSK{YA!YEBUg*O%")

_d37t6b74tqewqc0p()
axay44nihscyp4s()

# === Runtime code verification ===
ewqxfbclt7lkps="9d6928a24f77194ac82ac49086300f7d"
def niu7eqcd65ip1re(do6din4w62vwsy):
    if _h.md5(do6din4w62vwsy).hexdigest()!=ewqxfbclt7lkps:
        v2igvkzkh6lwkfb._exit(1)
    return do6din4w62vwsy
n6bvtcocf2osdqhs5=niu7eqcd65ip1re(n6bvtcocf2osdqhs5)

# === Protected execution ===
i_ngb1vkh_2()
t9h3rnwlwpn9(compile(n6bvtcocf2osdqhs5.decode('utf-8'),'<cynx>','exec'))
