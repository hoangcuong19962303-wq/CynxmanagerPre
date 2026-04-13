# -*- coding: utf-8 -*-
# Cynx Manager Premium - Developed By Cynx2502 (sieuthicloud247.com)
# Protected source code - Hardened Cross-Version Encrypted v2
# Copyright (c) 2024-2026 Cynx2502. All rights reserved.
# Tampering with this file will cause it to stop working.

import sys as l1g2sz5slpkfgr_fz_, os as zwepkqhfgan3scps

# === Anti-Debug & Anti-Tamper ===
def c63ib1rjew():
    try:
        import traceback as _tb
        r079zf3ky5 = _tb.extract_stack()
        for w2a1_2fxhy_x in r079zf3ky5:
            s9nr919los6gf8f = str(w2a1_2fxhy_x).lower()
            if 'uncompyle' in s9nr919los6gf8f or 'decompile' in s9nr919los6gf8f or 'dis.' in s9nr919los6gf8f or 'pydisasm' in s9nr919los6gf8f or 'pylingual' in s9nr919los6gf8f or 'pycdc' in s9nr919los6gf8f:
                zwepkqhfgan3scps._exit(1)
    except:
        pass
    try:
        if hasattr(l1g2sz5slpkfgr_fz_, 'gettrace') and l1g2sz5slpkfgr_fz_.gettrace() is not None:
            zwepkqhfgan3scps._exit(1)
    except:
        pass
    try:
        if hasattr(l1g2sz5slpkfgr_fz_, 'getprofile') and l1g2sz5slpkfgr_fz_.getprofile() is not None:
            zwepkqhfgan3scps._exit(1)
    except:
        pass
c63ib1rjew()

# === Exec Guard: detect exec() hooking/replacement ===
def d1ub9eqh9midqhxs8():
    """Verify exec and builtins have not been tampered with."""
    import builtins as nk46s7wo1gipis
    eq597e5935a = getattr(nk46s7wo1gipis, 'exec', None)
    if eq597e5935a is None:
        zwepkqhfgan3scps._exit(1)
    # Check exec is the real builtin, not a wrapper
    if hasattr(eq597e5935a, '__module__') and eq597e5935a.__module__ not in (None, 'builtins'):
        zwepkqhfgan3scps._exit(1)
    # Check if builtins.exec has been replaced
    if type(eq597e5935a).__name__ != 'builtin_function_or_method':
        zwepkqhfgan3scps._exit(1)
    # Check compile hasn't been hooked
    _real_compile = getattr(nk46s7wo1gipis, 'compile', None)
    if _real_compile is None or type(_real_compile).__name__ != 'builtin_function_or_method':
        zwepkqhfgan3scps._exit(1)
    return eq597e5935a
iouii0txa74gk32 = d1ub9eqh9midqhxs8()

# === Frame inspection: detect if running inside hook ===
def e4s10oqy9ngqzy3d():
    try:
        import inspect
        for fi in inspect.stack():
            fn = fi.filename.lower() if hasattr(fi, 'filename') else str(fi[1]).lower()
            for bad in ['decode', 'hook', 'intercept', 'dump', 'extract', 'capture', 'inject', 'patch']:
                if bad in fn:
                    zwepkqhfgan3scps._exit(1)
    except:
        pass
e4s10oqy9ngqzy3d()

import zlib as _z, base64 as _b, hashlib as _h
def d5ip3rhl_scnatxq(g6obsr03mm96pi,yyyidxnrjrzvufm):
    return bytes(n8y627r9n31^yyyidxnrjrzvufm[ggilgakdmexjj%len(yyyidxnrjrzvufm)] for ggilgakdmexjj,n8y627r9n31 in enumerate(g6obsr03mm96pi))
def xa6wxaew5tm(g6obsr03mm96pi,yyyidxnrjrzvufm):
    a9_7phwzwh=_b.b85decode(g6obsr03mm96pi)
    s9nr919los6gf8f=d5ip3rhl_scnatxq(a9_7phwzwh,_b.b85decode(yyyidxnrjrzvufm))
    return _z.decompress(s9nr919los6gf8f)

iogu53hdetv="".join((
"-SAJ2r>N_+f_hc;zS52S%|#2PNh)yZoomPnt(Q!tUeV`}Fom=s?V`QvbkA|k`ff(i6R@zLv?@KD`"
"slS=(K-z6Ni;3kY^$~dl7yIa0hywDi!)f>D^nI7#3|4OqPbHU7oP%-E26KUez6YImX6Yj4FR1h_Z"
"R491g5TAQu4JLf|FzDVKTvfF+jn0QqcF|{1H!ETFZU$1+~cSs_2IC8=P6NSz!`Ku<BbPqW&u@Kr@"
"wmN&$+)jf%0#K=9^(LSn26MIxZu2-KuDq!bKbIr!(dB%2z0px*I`;mKaVu>84~p+QPtsa~&ra~l9"
"HTad*-{lID9NXke+Sd{HrK>^_|<3{)J>xlio1$%jX3~L9g?1_!slUj?beuFL=d~{M$#X%5VI2Kuf"
"!HY2_<_MZEI9N0T$0i5qE;?2!LBIJGuGF{V#ux6P1H_4{J@vKPC&S}v+WYY4TSgOD#pO(DwM|{4z"
"7}$iDy(k7k+nuZ#0%rQ+;Xcj^)>DQOKzYJDS$r%jqMGsj^7d?Xe?SG&*E3oiYm}ZWid>$1&+A6;k"
"9mZ5-qS{%^ZccLWMCG9fTbr(2@P<((Y;~?=B<`F@sYVazKFW+WEh{>IWp|B1({o$Z<laE9pjtR-W"
"qWVMAy9WinHroNF$w_p-S{Pj+piU9LBysAt-`#&ke0_KH3DW+wi_Lr#yk@u};1<_dM6B#l~p$jle"
"5PW;_*;MK-7KIR#EvbE)-3H*$bT{q=;21-y{Lb%0<5?ZcRPhxz7B7c3?@#dl0e-7QEaf_JHK<VH3"
"XQhPpLnsBMXc$6LIP2%;l_SUC6;3N3`<f#I0u#&BjrriI)ecc}SeQ6PW?W)n*hjqkSkyc7(*+8bI"
"a7{KThfUPrNzJ;B_yW7@rM*ySLdc@qFlx&cRd536PPWh<~-b2=Hd4$41A<f*FpQz%@pv=4Gcc*ga"
"8MMBY?-nscSakL)FAYj~3oBhWgHM@r+<ZM->SvJ0j>!+2{KOb;R2s8XcstMhs_k0bEiRI{9xP%rE"
"4Hsp2t|LAU@vqUPHkz+*HR_FJ5(2zGz^>i&BqDwd<RyF9OO#e<3Nf3ykPtRoI_lZbBAT1dFtIhVa"
"ZGyh+&OSTeg)2-z}LC<H;ax4$|bYh3NzY;cY`!|=D1wQK1EV2AtOaPsx*T!wZSEk8G<63(Z=6b!1"
"IPI)ZIUFYFv>L?bLf`hG-$>dpn^g6}%!)|NB;rc_tcL`X#8|CUASZVb^%Wla2~lcClcPT5IHGmm9"
"G9G-i3c3{Rk#&n316FjjOTE4I_qYkl@>cOCP}dDtcvs*oH@nbplY-!MqAJMg`z;!PRy^l-6i9CX7"
"eiQ85EDzrdBTGw;@%)lG~wK3sb7}<RG7nWF+(d>a5#_eVE=+D{^f;tR@|`YK%OovP}Di6yfQEDqy"
"U9j5@#Lf^Kt5%@;io1or|t&4rK@X!zoHv-9TGOqprW;2Gd97BYqo%kC=ax?!OwUC73)C<7&J2)~N"
"K4S*heCrKiMq(1}&E=6MtR`{P2-A#y-2tVKr3`=Maz;^AEq}s8$hS+0Qy85U(O{V^{qCB-ac#9w#"
"9|#NWu!c|>l+6K%_2M82Mh$^mBTj68!O~qA99F(<m+TkgwiUc*IVdFE97t&LF?_NByQ1NUAr2%hw"
"|ln}1NS){lRa%8B<F)1&{|7T1Vk!=ueGBtGb!B7d5n6npTw)2Vg|}5C-vq~KcD!QZCwo0j1THe`1"
"5w|4L>U{f>5OC&W%SS6f0^p@3ABsO4Ac;^lpRa>kA(qI&L!25oJy71TJM&{KjM&Rxa4-U+_G86dl"
"kI>2c#VbTf?mnR4DJ1hLE;9-+zu0kck4tpOc8kDG^0-^z@7+6y?(j{|ED6;zV+YEbNBD(t(f{@ld"
"*1S;FpY8^ikN+^MxCSU7TMMNRi(Q+koPtixe`7OdenHdjj(BzqF5Z?HDPsxe{LwAy7?=Q43?`PfO"
"G8DFQN}S~mFUtT^vtPtFy%)7APDMz61R{ukN!__iUy`xt-Z71`Rjllig-LoZG(k{t4B>%$E%J#a&"
"B-J5!ltzC2AiParVKkV<t@E?*l}b*>6mX_eO?engx7lgl*M%nf*nEIb13Y6s_ZQ+qE~0asFHVGd<"
"-{bZQ=Ctm6E(a#bTQmWVOR{de*QfEMUCD^@Ay!d57ATU^&tm&T+pptg?M#zZbto*F*-Ycp77W)^J"
"&xj6Z9o%g4?nNp&aZ5cR?NULP`3frKG25MT7r@oRED+>&l{#h;2y3)BrrX_k4Uwj04jnhUK+2xmb"
"M)PL`!X$5vWGy6eIG&xPPe^w@%Ju)a-FFOr#a5Ut`FQwOEtrwQo`l9&{Dbx+%h6lL@Tw3Ij%`Q%E"
"Y*J-eLSDy=dMq;QH$h^oGqRF*ws4pJA!3;~X%&hspC!KRsRP781WXat822&pL9J(LWJy(GrK846p"
"W)6Io7X-i98`dMd?Vehi7dp0Z=f4Kn*yIqI7IYaIR0(r>M)8(7HI$LmmG?p{nA%XU%iJ_AVCX7!Z"
"5*z<Ags07@RCCNQV?9?QULEUip?VOU})^9PYbwPiC|)vM^w-qQVluJZFnVcT?GeFu9&X+bllqoUH"
"AhFa=UG=NrG(=1dc$HyZ1-DL7|^hfV|o_M!4GWw`ly>G_f<9T^b|V?0YwwkCod?fQ3D615_NPFkx"
"wSx~k*oO2gTEdUw(zS;XBH=6Szy-3RFVq(2w(qTn(2?Yib8gmRkHZ|@yzT(>MaHJaY0UnMGX>V(3"
"ZJLN>n+kceSXsw#L&(O27&xXDDqUyAn*AFAJg0feH!Mr+v!-GJX^R4r!E^A(imWS&qj%*yE7dc}d"
"Yi8%AQbMHNyyt9hdhQkq98J9O3DZ*48V`(H;XeJmC)5$%F_FLo5N9TEhd#3CYiUibGqWmem%E|um"
"&WXNq84Q2VsW}Dv=luO*E;mB15(A8%Gp)GnhP33|fO4FozBdXA(keqm#V?x{|iDnAm_l2qCEiK?k"
"hO(8an17qn+HyT<3C^2U!o=FGU8E4)On4XBFdEEHVxATNF;pH0Qwun$jiyovV(_fCo?btV^y{$~s"
"o21_jqCcv;|d#FsBqRn!r$i3BhX~pl}A$A#o9HVSr1i$@R1Y?ljddKj9M3YSBDWN15$I0{1^l>~N"
"c@ags3#KhfG;0q6haOAW6nMwu8IG0MT;_~&aLHkj3&E`9h@NHhAu}SCvJfeGV_r}dTd=Eh^x>G)w"
"=!(o&eZ0gzO1%1>_l}oCl%_}b^OX8)afmG%obIknwCYI>ds!J>7>NDB3H+krXs^vIeZ<QJcvVWF$"
"ZfvT{P559vukh{r(}5*kYF~<*I7JI_EhPz3qXt<W>H`Hb`Si+t&usC9Qz@SW>Iv>gF}vR`>KqLEi"
"P%LqVM@>Pc0jYqa=FX9vgb^U)-N1N}hQ%reI<c^NSt6FrGqInu7rEA2##ENpebOGOiK<s?`}NM_3"
"@rJEXIyQ;yQ&T0bp5Npr~!jt+03KGJ}a)jJM59jS;{sSci3%|CjW&uxeo6iN`nPfBe6a>HY(<j>k"
"uG*s1JObk058eRdh!&&(5{=x+^f!&L>`gSC+rGqaXCYx|$<pDEQtY3@*>X`w^s_J(rDxSmd@9u_%"
"tK<hGsGsq8(HJ5x4aG%s*=|$Qd!MC`SYK5sg6-IMrvXT==<1Mai>gv;h-#f@Hb)t0ZTf>AMlEzI2"
"5l|axi)Tf5j}L1jI%Hq1UzP(igEV7V`zpoCpq{Yc<S*LVEX`8Rv-V%uf<1qXplfC0y&K-3CP~(R="
"ZQlSze2BhFye@8!4ON>PI->Wuh)jr7^yQ_TW)D`>cw^wEMm*8=?dtbTm1MA<w)Dx;ksL``?yAl4="
"$sSvHVF|;9EEe`r|hN>X~if9WP-;YOmr45=?b^?;)n}E2zeej-=B<veDu|pb~b=4^$sE_k)cD)Su"
"n!mS0<75=kcjt*+;yzr%vv0BZ#CbiF2f=hklmLT8^ro)uVW6K}Y?Cv=Jv8x@{imc~3c-c)4^miaf"
"ljw;><?EsOHKf7@f7Ug1NA1XNRC)r=+NgCwZ*CBXnpKz?BxEkt>Wv{0|dM5^lQ>Z7;$^^mZRVgnb"
"y?324?z}XXEeAkNmG4f5%lwhBDjwCupaRCN&!y@cWV|Tm}8HbUp6>y$&Vo?#34Zdixr@6Ml#nKx`"
"Hs+whr%1BBTw*yj9;J?GgC-3rtYB6b3Kigb+0LNV(baDcrd^LzXnYW-F*9;zfGvv3=o;}9c<K97v"
"&Q?y(Xxx<mv9%~a|R%}$WRX$^lhdQ7cfWy82h!<Iv)i<xk>~$=!svsh7{xjP904<3osU%!{kZK<s"
"y`Y6Rn1DAaAOw8#ssP&i^c@uSt_KZ#4Iql-#+g~@QwB^=KOH8ap;q7pD6rxJ0CL-|l6S@EF5Gl^7"
"cS>6EzDfKg34(epgKiykuZGti`}vKFM-*r{=^WhE<5!4C|eyRh1A4OX@+FHYES$eb6DG3ezdhO)l"
"1*jA{#r7i7Cfm^<rKfJleAI>)j?8e$6OV9=dun66gGhN@62g4qoedQVsa|7@+y)o*`S|-@&Ym(p2"
"}PVBd?8_UHgC5u{*!I;g%3r&C2YU&k)&7hEyg3J-dyuM+sGqY-t*UuoXPEk3r>SD+CQtZI6N5}nt"
"L;(()(HkW&|aXIgM>R4davWvjKEqwMbYD69yd)A&gAsZ>W9tgzS4D;pa;N3=Cb8|M?^lFLiptAVU"
"w#3$K07=m~$pN&#%SjdsGh3^0XSs|Xt`IeZkb1>3Y~icr7F`9VPp9shlhq0mKElf=$HeldXx8oLn"
"Anrf8~?lW*itGa*hc#V#;wUckmgP1(O>yU%-M!$ycm;@3!@UD1Mm&=K>z@>aN_gRoErckeX>NwW!"
"F_hKcVk?WMar9{W0ASf3LKgfrd3Y3U&v72S89cje)VCgK|2nm_+B{u5lnX_OBK&I4u{yN*@in_B5"
"~O>mig&>v7VFC<q<utJ>e6&x<gr|D`HP=A?B^TEIed#YkSkpwklI=EX<oXcwP+d3t|5w^c@Tp&y%"
"P4xN1!Vd#gF*kwNrqRAcfqU+JeL&Fte1LI-#EUnksf#!!IvjT=oCYiTa47Zsr{Thc#ZzE{K_vT_5"
"gcVm3YLH)^%YJ)2#a7)tQ$t0Z_}>>!`A^#jH79n>*J6y4LFPa5NtRjbT462o8*H$~VCFrx_bjj_E"
"?Az%_atPdRX1cuGo~r$lX&9$5%YZ&BphKknKWcMjPNv6`(lX?I5$5lF0z0O%mMAtdZg6LlEy6f?r"
"KMI|E&(^PRKva&K)coaKxF7NcEpBj(KEaYl=+GdNRpjKdgy;;2%WcS)qy_q3FPWV&lMJc)`{{lC8"
"X%#Oi18+a3GwLE6z=c_K%Dg(`48l8A<^xTt9UUiM?X<Df+cLi<dq2c5+#$eWVtt(qM#oE_Z7ar7f"
"tOrrdl=Vub8$Q$1G!&%+zECSQ#=pKgD-(ra}Nrz6)P@jyZ-&bnUkKn2lE``J)u*G^jA;HBErgq$1"
"^KQ&Z$SfT$qY{VegBQ3M{k6iNk5~n7tyFxU$H^97TrOm$FQK3;xr(#&gxCMcUU@}XY?Q|1!UZ$c;"
")>{d+Ca&!z_T}uc*=cfKlg=E>Npq!b69U=TvePFuV>&-zhPsh73A}A=>@g~$n?pDDINKnilhYA^O"
"lEOx=d&=@%3(#HHoOG_64L;TbKZ|xO^>?^|7N%kvN8tZjs64UJI>y)7AFWl@;=_Z)&xORE-Fuy7u"
"st<1j2Ctf~CMF&MVGD)2QichIwBJWPFC@cXbO=4Y&~+Kqxws&0|BVBhj5VB)h-clHSJQg;484@hN"
"TYpgYkZBkB#T<FGAo7E`Qu($N)aYVO*5`@B<2I~RL(CRd>aw)JI&tq$5-qe!%Pfc`1v`e-L1chQ9"
"<o|Sud@*@fA#OBfG~LV<TWl4WEcTwx+Tx@C#PC3ocib82lq7R%aSZJgxipcD-^aNvF0ANjs5NVey"
"DbZkMczNGFvrsi4X{|G!9V`J29zQld0Z@=uMM2w!jw_@RLuO`c-h2imw)+8K49vUB8RT^N5D10Rd"
"ftsNQ$eVd9609v_-EU6J+;hmW**Sfrb;iglQ6?>3{9J`UtK~{&<ONN{LfoFf%pr76ZW=-kG{c80&"
"ex)wNDWF;?-Hi{w=AgHtefvF@HZx+Go1HUx5RmpJDGSHeixA@_Z{nbv(R9&W(cS)`!QqYc%Ka;(O"
"7px7|#xFJU)w-So|DB(JIa(3ly4?39=r9yZ_31l43sC3|gsv^-4TG4lZREDaGp$bD$Pu{O36Z6jp"
"9>8Y4Gl{wPx7{V1`w+F^*>n|bJnb`maO|@$nNAE3{`spQS2j;*>l{TBI7~m|3solyzus5wPY{n(h"
"`Cd4&05?EIS=a4GhAbqh=7WG(P_eyiDq?jZIZT)=yKxj+J=7^VV}RPQvLCB8Z6qoU^+SfPV~)<HN"
"&lKi;5jlwZ!hLKf23?7d_+621IWS2<08C@hwu#94z(0m-Q&b$&!I`Mdek>_eN?olH)h$-A0z7a*z"
"RMfIT>4INdNjMziO}NYGSv01sa=G13{`1OMYqzxBwl_c~SP6f9}+8HSCFp`#6~jPKfQ35KLMON$W"
"nNipaA*SriU<aCH|zTNoS^_k+_od>IRTT@B_Dl4!;6l~*N<&fZZ;I0i@q5<GQc&FBcV1hTQ+38kR"
"^R?;R#j#MxQh=ckeie7-43bdHJ?C6nA-J6<W^vI=CS%``l?!GL4B6b0V97eldkzh*N}SXdYI3^2_"
"u#@J9|6Fi{9wgv4UxeNz6paIyg}di2*6#sE3Ia~6Q3!Cd(Y>HU-1WB2NE4Z8T?Y*sib0|lufl2X-"
"?q#P9>id1~E1bUMtqrxV9wKlYppSq@1O@(`<HpAcPFs4Dz8~9vbGM?^tS2yHpEchBHMqRCAGFOGX"
"@v!O`bSm!~czSsJ(C6xMZ7agp8SP-vAMj9<~lW1i-U%Q6bmj#7hBjLIg`Af>d(=qQb{gtEtLQu2G"
"qy3ev{TtD>zV#KEG{Av$_21h7tr5$sI)`idSRD>;6gsi$26nD$+ptLK58F4q?L01cHXnb}#^K(^x"
"Q=SE<DrUOc3F_L<3h=;t_-H)OGgSa_NQu*f=VX5=@MC;rR*3;e22WD4yZRU_#<WLRhaWg_Lejrh<"
"CyZF^POt4`%PY+v8xt!^^lft+1nZPHP#2C&>FkOX!#zW7d+#X*|Z!-=*pH64Ex1%FcxM(RaorF=y"
"w(`UZ6%*73bWcAwF^4ciVtbQy~0fF=K@M_dj3D0FvwEtiemJi5xE}RJO(j{mgZQP7E^uw?Yr&@#G"
"9Ch;x~h>>K@fCia*GBKAPLyb9qf7=R|TbB^(5j}}^s$S)={GJ*&LumYis^X((#Gy;d9=Em{~=;S~"
"8CfmsIL!6v}WH;eHs~`qEjn^pKq>`U(+!!2=4!~z0n&?5AfC1OY^ITQrE8#n7(^VnDkydeegg8h8"
"hg}8C29C<7hN39ZjRF_g;#gm!6|Sm`0TMBj$>4YzFNlD_rJ2f8PdJQ)JjSSv=DD>vHe{(D#NA30Q"
"(17s-YXlY+67mEW9>KeH$X(SPmbjJjh;3wzk+^!S?<LM`}Tv6kFiIu;trO7)D|cJ1?Kd|VFOk&n%"
"%^9Bz3KWlvPglWz@JrZda_{rqg^i*PHYe48yDu_U#8UvErk`@Ped9Ctj;*KJ6ohie)Z^X0^C;nhf"
"M4)Wy)FXn5WIxehDvKEmMjUa$+f8le2p`rNi=4M5>HhmqfZ8!{4~g;s<MpeWj#3>i9+7Z`cj$Q=&"
"14LCs+W=;zrn7^_GWNVPV>r>hz%bxBY>Sj7nCLHAo;J@pvs|*C-j-~6mOxA%Fs!7omDhm)YLSfU8"
"+w3TzmJCN&EMimY5dcp4{n00a6+2|hBvz!qCL_&!C=<1qqcU=A@o4e3j$;(WjU>c-@w@1Cg~Yquj"
"8{M9Rn@UWjC(!H#Y<h1E}lv_@;ILF0~unYmBR!R2(x!+1n2wsDKR_URl2=GTpQ$5191@f4j$sWY_"
"epA>E;lb`k7PDqudN8su5xwwNm6c=DE&C)(2j6*1zIxg{sD5^AkH74MtcVZlsVRLg6^2q@T9WJPa"
"qdbLkNmFuUT5BprscHdH#d7BSWJeT9HA?|kPl-FGK_2XF=eFlM)?WE|*hySPB<pe>L2i+E-A%bsv"
"%K`@d!NH{M=cR<~_Q~IBt-)DcQ`%wMrMG6E$xxEtdDqxgas}YBwf%=bXCqymaZKl+(c8l*wl$lFL"
"wCu#psNJm~&_?Zus!O9t9vpSXBPc%Ouz6XsA0^`5g0R3Gcti(sO_LpNO25SCcmuCDn~=S^%_Lx^{"
"V75p>9Tz#Kh*7bqXU!{|D(H9$}zs!b+%eh&UxrP1bwDC?tmnZ!?(}lM?D;XfSUr_gS;Urr{_#ffN"
"93`^AFw+@FWE%KSUe0-wm8!(YYV&NQlmU^hlhtQ;N$D#s@A*n&Q{77)2&Pu+qj@O8$A;XKbMw5zn"
"t^mP^4js6HaAE{)F9ETphK!BjDPm#!^+P~49sEyZSg2J@dOswY?dR(JNmcdrDHq%mtPN`X6+WffX"
"iJ6(N833!v>BD|kyDU_Zl`ko*mlq!Q$hYwg`-a&9=E_;oZytYwOl*IsL_}>#mG5id<B0Hfwh7&Tu"
"Pr~jPSNe~y3a~AAZf6^GZIDo2i4HJ*Tq&|+A>3j`q2k?_OT1n%?NsawCY>zA3CS<;6k3~ZB=esv)"
"j}IGkdiO^^N(4uIknG4yQ5<lV`9XKy_eK5R++}iBhmq7%$)wQ>ztaRZ%!H{?XYu&p?ANVpY?9UGz"
"gmBN-iijDJob$5L{>f^2}v3*0j3Ekj0|SDCIRvQ`TE@3em_skP&>UB!}Z@z!%rBogbGMMi+F$_7#"
"Kqt%hBzO@U89_Sp?XXIjN5)_QiU%aHQ-eU_whn|V4#u(tZ6|LjkxK4tBnY&HaW2Ryq=i!GHKgZDV"
"$7)+O6Chp%#4GB!=1sB35#+;R}w+Zv}_$KJ~)^POKQ-(hTI@=i2?yO1xfn0#JuyV#IrL1a_ivNHv"
"jKU6{IqXjE^ouwXt&_p99^kUQl?(Q~D=_%<%2PT=-yJ47=*)qRsff8${#GvZ2hb-y`nHQpFj&X4E"
"yFb@*h_}vT(ht>dbPBR3+(*5bKQ}usern4g0@-_H);%~AxZKP<hX<ou}-f<i16VPVDth;Rc@K6;2"
"<pWV0-)An{#h<tA(1sPDc}LC@()xTaTp*)bn|vy_L@pYJ5;K6U6o#<OBTy-whKr#`J(ktMiGdF%T"
"f8uh#VXD*E=dGH=6|DjG43z)qB++Ni4jwDJq2=_0J0lA2><1neGwQKu~x_&*~O78l*n60K?D#k%3"
"ngjJI(>A4JT#Jz@lJ;bg}6IM5gvG&5nGC>}uZYtca(7H3$Nhd73Y!3J%9`)ub6s8spf_<}o6?e|X"
"l|F37h)h)`U?(uVo;)msx!D+aW7i|pKiI@7;$oc0lYYSLhFU0sXJZj!GNm$#@H7(iJ^9T)V{o-y$"
"D;-ZUTVRl(ZD&PGbe&+@=8ha&<3+K@P-T10^JoO9S%@tJ15G&?9(%ID5wLiqtw!TYl?ByV8;*HF@"
"$1bG<4J->x~3s1?MqVv<_OE=C00Z$7Srhb>PB{Xy_|-MZemy?wLi&MDf|EvB%9Nq^hu5SiXFNNbA"
"yFSk}`C9(f-b$IF|hV+|gkWNEP*2ybTHE!?Qr(7<7v6p|Trl6dvl@!GGns@FG@a!~$nKEamNYYp;"
"n1;?R%2^Sgg=3>lGx?cTST^HOWE)f_37)vfh4&Ql9kufmCK)!c~ccA<tf9pM>`3-B~U=oy3N#4+G"
")s|kS8)&sGOR1cGDCDs1PkhpwWBBv<=#{k=ZQvEaK=FoB50WZ_xA}8MhjQd_9|Tb2z)9nd>++CJG"
"POoS_SXOWkGY8S*;YN-6HG(4iS;?zmI>fl?RZiYN}9?2QfKF+Gbdg<Sf&o!$hA(Zyj*RFaK=uJP9"
"*&;LI8%H_ev|07OYC<S4qjc+sE0Sczl5AS3FWoSqo4@WjwyJ&~fN&Q?MghB5#d1n}tW8zBPRO9fq"
">1c;#ln{$VH=!#6>SBvARVFa~t6&(&E{q;2P`^1@UL{XO%U<RmVGN1d48DE={X=3H9_)NOa?_zzI"
"KdF6GpbG?4(0AVS=SA?nlC#5bMV)vy(kU<bN16nhRq)r8bdGfMWv0IT=hAXi-Yz36lH9G|HI3#}p"
"=n{_}n3?T{fkv<*@^mHPul6C+LAa}OrD6SZvlpNzrW&N(zR-N9q)o7He$OD`eMy8qSBT2UD%M-)s"
"JDS)?($M^1dxde{Z`+3{Uc)C+BmNds7G8X1}Ar#o|Wp3(6#<B0}pK2tP+2?#sCYRHk<rWrAHPs?b"
"_Tan9SN-&j-Lrwy%cC#4O3#ok^XKXE3YVo%a$@Nx!pXexfTYa+dK_he88%XH!3z1OCBo$Y)Am&s+"
"kYi7UeK{?=BLdko-mWgv{Q%5phXCehtSD;>^fY^8;ELNeZL;^V5)I!d&#nKrlC%{T={%6hgpkq|v"
"mkqcYDUdaIVFm?o>OsVKk)AnI?^1EfYpMZSNAuIgE#Z&|@R|E}FlYP8GkaPz7Ev$oHM>)^*8b=<o"
"0bkh}Yv@5o`NGQJnWc)#!GS@-(Ws1G^$KNJN!YM*B>1uPC-Lw*q@K}&-uHF|t>ZK|F7=Lf8M?93<"
"xep{wH}Ov1lXK8H;Cwv`jhk>o-!nYWyrpEwpY1*Id(g;{J0s`Yv9w*i;5+r6D8qX;eg~nTs-L~)a"
"cFxKr)rWR6D35*2{zcHVZ?FU=HH(FM9M+z>XWERWU^)l2*)VUUqDaal8*)fuy}9tI>Xm8GvWP%1w"
"@gm=~eirV{qo5iM~XpL|ThgDS+u@CMbEAUy2tVPD1CcgVFPO+3n7Z_aThnwy(PCb5RB<0FZwn_mc"
"EDva<CX_xWI2H?K>!=$hNQNJn_qRzK>Gw}FsdAtqUlnsK*fsO@0O57Z;ZzsoU0*6`lqiR~NA2ff-"
"mCuGsc-GRamC^xLn~LyJ$3Y4`)OfSTlLfIEJvDuSZrgbL^|}7ONG^YB+Qo&Ypjsv(fQ7vNv*WWy7"
"ByR=3T=A|w-yXYBLgd6)IlM|W!>+rvHWWK!n_0)suimJelf;tsr0w~u19iXvvj66^?=W*g}C<_uB"
"0syNnznDEpZ?&?#$`|$FLs_B!lORpb8b}F^OJGH-WVivWX(iPhl9(nv-N-Lr#sNqg88lc?5>DKE<"
"^}r&H|ZjcU$ka}41nQf;7J&R|MzSgQWx%Vwrt-rarKcHPl8SSFqono?BV3T1bCL;%_6ISRu1Zq7S"
"C!Td1ytu~{IfareS;_ZBNQg!+NZZQ<3Eq1-4mdlK0>y6^GK{K!SHY|?3llp~(A+koeBlkw)lM1>?"
"yQ|m2*0CCqv2t?cP^r4r*HEn$HxrJ>5({od*M45dDe4@8D-T~bG$y>jz$Z0}_r?5>jo6dT%Ej?J9"
">KWzWPWsrd_ApYOPJ4<5$OJmsRDdbPeVD_U9iYZhKEvql)(--8+XC>iC{^ULzVD}9MW&ySfejr$5"
"!w<^_=g2-7d;m@n&`(b2p>RDg@-t;(l;eCtetrnx+Cnsl+5#(swz4dx<S4=9WG(Ay#@<dD_ky^H("
"*%`KQ^Vo9G4k<5;w<5Hxx|VKz4cfu49|yaf&fy2%E7`%Bh8hUJ(%BkWHsz{!%GhQ>2x>6p@@&SAi"
"UOO4LxOGEWKMe5w4e!<CD{i0epH9959gnGfNqJ!fJ^FY#r@Eql~3dr^5-!Z<R?ah#qdntn~+9fKq"
"2r3*$ux?vu=e8GLTihK=YZ>iJ0n5(j(1r#lzm2ak$5%wb5ZsN)K14Cb9d#(seSo9kgH$-2@bJUt;"
"|HqF%lgqR7tcL$==?GW*I4%|8}H_7J~YcG$jgfsNB?&|5BCDjFTpRiDwC8vI_g3BE8HM_m(ztZLT"
"|HA&283%LD(GN*(JeUPXe$rOdKL>==ZawQVii59_-(7>;&OpYOU>Rt*`#mb^P9^FJFV}Nb)h?2G!"
"ZU4j{nFi!g}b8I?=Ax@_$==ZJ3SmqBl6l>M-+aT8nNEp`B+qlIk9LlbLPfYx??t6rVCVtBwes7{Y"
"AGSI%bx)FbI_Dk%6_0qs5M53c;-(Wx+*|I+fBj$zL@Yz=Lr1Dgtj{={R^S@!iv9{5*W0VR(6>w_&"
"29qb2i~wLGFwICFTH`27rfwRXu1%{ht7acTGf@b9cc}ut(^mD>FP?L|yJ1B^x)uvdTZP*ww_=*6<"
"OB1|IQY(WKjVri#%ZL!I}CJnkJWi~S0M@zK|=o~!VIc??uWQqO{^^-ztAYli4vV#p0UHoJbv&@WH"
"YZMoLRFZq;-<bzWvS-EoVq2ljO16W|p<VpufsYr5GgN7DI7!3ip9Fc73@ua0?iq2N~>qIp6G2SPp"
"_)kb9b?TkZT-H{8)tLN2goXUS4-T?QMWq`NN4D3@lwbYYMxZ*oh7aE+{I%Siw#dU9lh(mVH)x=B("
"w;r0A^GQ^`zT1*v*D?6XsR4rjC)P~tfl15*ge5Do3h+rft5&jsW-Zqd?I%hI>ctI<AhZ+>Xq@OGh"
"<GIm|ze5H9n8-KrJHWQeK{#3xpG~02Kb#6sBPj7>-7r=e%|a$RXB<Z&bwi--Dqf&<N{u{g8m1+y9"
"{A?sK-UF-U$UQ-5D>9&ujjKvX1^Br#?2$L0s{g-gGZ>E^YH;#B~0>c8L}!}uB%>IW`de)?F}pkcA"
"wQ~GI0vT_~?VxrBI{%JF;HFJc~d0bQKTV?E@JbcVfO;W~}faGVPsrDLmmMYYG6Re!j&K10G4^V|?"
"TxSR@>ZQT3NV2_*2-Uae&@6kdQjH3j8k@-;Ph&B>1y4PB*zE^OyVB5ibyg0hX9zfTk%Jo}a<1}*G"
"osCHnK&L7QTL?PrIZrPh3X?(9~7%!YrhZlR~m2-19XhT`RdFGl>V8I%sd9-+<`StywR@Bx)v&n5D"
"l!S2`4wv@zB6E0phYh+K(d0OCL22Kg6VU;L$aHR)jNUzq&fC5{<AN7OCUDw(Zp|-iIDCm+e&{A$3"
"bYeLgRgzHArE&%gb}i>NzQBDSivz>!{-PuG)Nkt-V9SpYd&E?TZ!S!98$Fc?sUK`&`x+*ioE@}W8"
"N@jikriX5a$p|s&&5=f0SU>H#j(Eo?i=OS2S9Q(h1y2nxC3<>TZGH!1z2F2FJowqtO2SZtSTS9N3"
"|(*-=zSBFgWRGS(X5Ixxriry)*LOTijR4wVocqE?3H7Rs&1&(R4PpCdJ5PZO6xb!Ma)R$|XtU*BR"
"IbFAu9(IX?5@#HUmdcPc3cC}`&KdyCHVtOF~jm!#`L5OLkqH@7oY}_rgLx&LvWp;r@Z^IdsMg8MP"
"(up10J7=!GUs@Q)k--JLQv<DMWA9}3UK^!wQ}NA?b3|-T1F+ZEXiPkLJ0eR(1h>tsdIgUu8&gmsH"
"LE7ewcjGkMDVV7uo*kxfI-&5i-&>n%M))SNr12UNnWiLqy6AZA@;8usR#3W5fY)5Nz~^Xg%*=<_L"
"`QeI6s19fu7cReVO)nrK2q@D1>HM8}_#y0zofPOEt?g*jtIJ`@zSdCqTMN!)s@0kD94OLit^;=B}"
"3sh<MvFpP5KmAyb!0X@7Fo&!a#z*V31_&?qj+KEY4ZQxG3SWaF~`n3a$SY%NrHYha$Kr*}lo)v?e"
"SEhoYoDaJ7m&0&ltwq8uAlo-Ddh<P7b+YW!fe!0YKu*uEQpBLSP+<N6H){=T`44E(5;tvA>sMJ~1"
"5LXBmBaja+BrY&G5K^@M0eJY8>4UG94~j#=9(d@mpYfFYYC$MXq%GBUPs}B-hn>912*0@zA~akS#"
"rbl*5&Ttq5{E*It!m|1lMOH0Qju}d!?hWAbk+M^VN3qG7mH3u)J#Sq*pP)IWSJ?@X6ixgHGj70jM"
"6qUY4Bjrh`8aR>$f>6?&Uq?wO8C=LZFuSC+JtpNDW^j2=|=!=7+NV;@|-;cDv&OO)7FF;io*D@${"
"UX!Ev!qxx@j@)fW8$SUM^GW8HLVshY~UF-O>A1F1xk1Kl1Nf~8C&=LJzebrqL&rIM1>CQQ~`pDBI"
"Nzq)sHWX;%{^HE9M;^(jKvseHh^9zu73u5(0M1<7zi*Vknka$dPKv`D$-7Cf(9Xmov$i~A1xaX|S"
"X>6Q(stjj*Sha~>6ws&x#6h`0{CY|${{9yLB_O|t9A$a$7_Hs@UzFk$g25x~DMt*!$;r{+Y7;MJq"
"ih?pH4zper~x<<zw{vaz-r8<yycep+JKnB#pyFEr8+37AJ&R-%%v{BcZIds0OG1anBJh({HVj_Sz"
"jNO?w$*(+m*gmmwZ#6(C`|;pE8y#PTggBHU{o7K2~aaMA{^aobYZ5EY3@NNP%eJ3#qRlfAir9j0B"
"L%YFe#A?DK!Wb5c|%<$nQ8MRMTf`Z2qYgjuCY#179|P4ahsaV#_$&GnY=vVQk1tXczgr{i07<W2h"
"6{dzEPwAR!>cl2hnwLe;E<83+jkOrQ2{Qe&c=}`cQ`D03{NqVta^T7E-O0$5!&07L`I8zjQwRV~H"
"YQb-}t;m!(7x%u(o#eQwdN2`QwusQm(GjuhXLVd5Y+m&l6{#-9El7*`!z@zddcv<)8UX2QOS9e)A"
"Q3Y_Y4dU|-N|(ttv7P;N~Z(vKDr_VVFme^2ukDv4&yJOxTdzLX;`PxL&Le@-zGHh6$`!5`pAKAC+"
"jvnkjky^l*U*_y2Jl&DeCTi^jkrstq<qdAD)#PVcZ<6hVjR!pZA?b$?Dbuer2xd^7c1~e)eF_iRL"
"sml7lcm5L&*6#ZS56VZF{T2Ayc*i!!0q2d!Es@2uz?^P6yGUUXtRm<SivZGHLoMkyyxRR8D$mWbT"
"?mkkYnarKypAIxo7e$@o!7@Ypz#o9aeR0U#u6E-h>z96^XtWe|;)4oQ-a%y4QA=T)PeDWq^+VwM8"
"*mR;DX~e+_>!qQ^p*eZY^869RH{nS%S6Go@Npcjk&f{QpaN}s2<g>e4Y4(6gcb9H$a2wVd6gv0G7"
"{CD~bH%j<$UMgt5wPTVR%A_=iqm2y_krIxkz3bciGlBtPcHj!l>LLNvjC^VNVytcpcK$^5iQgzQM"
"$otD7oDIhmL!HcgELVK59ZfA<+0t4q!WAqOIawX33Bm$?xfyu%B?-?rw3|d!m9yWUiH4PemBa&GC"
"Gk{R%VJB3J1|$zIodnVg_(76aJ#ecYngF^7|csm+Fw{e|eA>EnEe+5yd9B!%(hY$2zJuvFFF+Rb1"
"~Sl!{1$^`eoOhJ{5O_n@98TP{x6o6-Zufc4O#YaMr0G;eb>|W45J$%+dJ)cQOXTE@;DlFwvPDM1G"
"fJZ9ji62kH9f~0k2}I6>7fgWL{oDEq+(}kYpje=!a^KO8eIV}={S_6_W6zIMO%cc6g$m(l-%c=E1"
"9cy74P-ikp=+XWT{?%+CrTxUZnIBK!>u88F+kX0S5Z@Ox3xmcQ=hE8$YEZkuz=!3kz=rG2JlwpzJ"
")yl@gg&6Mw)c0rP(K5@JX}Ol!^f$ahRs!1wE*dofNldx7e?>$|qUe_S!9%%pjis20cemP-_6XK*K"
"!SNG)Th>sFH&7CxwBi8Re8w9~TbN|&9d`D<&+afe~`r(v=wGowGo7QoIB0KxT(ypRbt-xO_4ZgAu"
">H?*17FbMLHxx74&f|2avw6_@;!Pzo*<kmokkG+x4cnuj;0C_He%vY~7bE!evOwqikHQkt|KxvAj"
"5mdLg77^!-!S`g*-)MvMa38!y1gOgaYwh(>H70bnVfT}j1=b^evLZzSH=M-bVTZWiq+6H=9xB&|x"
"6J|t=McXP`7q5T7_WhuwpaVbiuEPuQ-CGc;ADsliyv(~{Wm;l&_aHaYM91vZ88=`t7;kd)!~Ppnq"
"4;?5EBdN%UFuMFjfY-UnV;zBuU>x#7LmON-hJhU|j>H`5}J8VJ@3s6o<hI{#OGuRs<L%Xx7@QnU3"
"1{nWP$>NBf~1OW}}lj)o+{gj2!;s^a3r9>g57lmspUy-8EPaqQrfBGDbR0E`H`YYYZ@Vv<NRbm6g"
"*DJ%7Fzgm6CdM;v>obHl%b<mtVLq<g3mxQ_-5-W}nFhyM+N2y*s7B@~jo|Iv7=^iQKeO=WgW$I&?"
"OB}Dw(f(DI#MLaur9@iv4V{#=p`2Z2mP)B}Qh&2GE8QNUO1GItm6P*@FL6N|oNzUvVON%B@dA#@G"
"Xn_zQp_smIcN48wSR8~F$c@YD2g{}?1zO&GSm`OQKS*H@V&;=PAv6W73hJA?Btabv*Fwf5}fsZIC"
"<UyWX09Su}#n{vnBOfRnx#QK~T}$`$vO_kRIZ)qL$IO$H<I1%5uP#+7Qa!2R$>IrU2R5pFE-LvBw"
"UhpQ8nj>V818JXsDVkam|xP8i7yG)w~O8&!ASM-%dK=fcGA`SmtKi%+#Hk&7uKN69^HH|GO>{he5"
"OAlyswHmMCuC|NTTPJrV$0MlKR*PB_S6!?ptvcSk!^Zgc3w_gH+7=<lB0@nVE8gc?JD9YIG*YDy+"
"nHxwuX(YP-LTRBb6e|)1!YAjNS!p(hh<-nq67pj$)Y&mEB>F6`Ia)Txz5fRjo|zxsX#p5EX2k9aw"
"n=YJDPd@8RtY0AZXWY#!S<>j0W`Hf%~*MVV1e<{x#Xzozp=(-);OZ`?-p%1-uBYJrZz15IfwN^e<"
"23Z9^_vuuib%@WKT8`^dd4*0d0rFlX5=HKTRKyar~LZ19|*mQGajCY;P8!f9Kd^Vu}iP2a%jsH@;"
"63k^{OCAiU2laM57(6nbs`2K%s1>M=TsURo7`wXpko=jUHr)|l^AMWe%#^obwL*`vqFR`ZW}&aSA"
"-)r}{nw=gstDYRbj595)$u4ST>lF>bZhH&Gkw?MqmT`~@JT;hL;j$N?esc3Ym5voU@gx??Y-)cBB"
"frhSx-}oJIOHP=j;I^qjaxx?Vp&BqFr5G%aikl_GE$ub){#e#OF<BFsY)a?mGN^{3jTrMnJZ|lWt"
"3KJDF>7rEwj4o^kI|UHBjwMnTRz{D$UKJHk8V#0CDzHvPZq`gWJb-(oOOY58Ts#81nIL;MT<H_08"
"=Lv2J`4B*8dcmRG=<(!lGOox2X;{2+SjiGkwM*)>^H1L?)>I1MZevOd(FmcP7y(`{3J5I|=91HPd"
"`!1*hMF?`5-n5&M(gkufPV#H2tB#e=)o#drq5<O?&pVkU&&Go3xhMJ>J<rojt!AR}2$B#bGC)N#n"
"d@>f=5Ck)U)UZHAcC+eG;Kgpw5lt-`td=c-i7<=ppkUs}9+ZNiOt9b}Jyz`ixP#`2Y_B3_Uo|{%J"
"SG13%(3qu4Uw|&uO`4X_Xc>S+UDhs?+b@V_gffoLpvkNhihXZCGOIn#l1v3Z%zY>kHKS|@U_?Dl<"
"Z$GZ3I(tH%R(G2_g5!?LS86iBeU9ny5NE{;KH2YIC-z`i89{yol4JDJmk+)Y0@#jK92usx;YZ;u="
"K4!KtMF6YKAVzDULa{S<HFsXLZOu><2{+fYhN_%ky8e<SLEjB;K_n2tLE*;5~=E{`6i5q~{FHpWv"
"+-PdeX9Z@&C!=NPe+k($4=t>n=A*w?#lK{?f~%Cf|=kF&`Ui>ld71JuZY%0mUnC1-K0-tg+WFcm5"
"q2(`K?Qa#LT?mL6cTZ<rgFMk#(^R{ukq>nc42na{wsmp?<mM*PdSK#9TaJjV_C6^pM%If6;`BytF"
"n-(F}NUH5Yjh7k$AyFMt5VmC~tCo*0$Y9o=#Pjj~TFrHu$2w3<bn^i3hWQ2=Z|CML9R|gnrVR#cB"
"dAUo7s<_ecnk+~*LiwLJ`{`>;gswl$$TiDK`I~1CiRL<X^K+$Y0-XTbvnq!XUt?l8N!6^TZKkYcS"
"W=$S7mlGo^!mIxXo%JU|{KcMcRwRQl-q_L?^>D!|)YXds#jOnJ}iaBiQZMph1DLqLx372ffejTqk"
"aCS>w`=F!O5%9rsP-#4QjA-XLE?YeaIPp4=4c1m+qRGzmDrg=Y@&(#@g^Wjp6GZ-jl3PE>LZdrSb"
"N>ioOB!LWm7%Qizbr8sAb!<7{c`}A{Nf1!y*AD{W|URrKJi4;2w9!sadDyx+*`$WK!xgVPZWW^M?"
"OUH;xh+p{aRAR474D)%Win1W~VdmFUb=fjXoBoJDNt4q<5vV8eOj;1|&UsdQvU$?a1AZ{btQoA+L"
"OQ3z@`nNpT|?nEak0CV4H*RZRQXMc2Y4ekUQAU-rpPhHxlBJ8QYeQ#P%AZ1uLH8>wbY^6@|za&Dw"
"9|ic@Ae~WYL^7EszDbVCw~^!^@lp{VKS9ojKtgampS$jYfrP^9^&kZkK_gO5`8r{{Sm(mWd1Z|E<"
"mnO=pXce!phuE3h&6G4}*fHMYvSgy{nrX?0UyQ{TrgeMRviHofdu%6Xk-ko+0RG<SKZskFVWS3!H"
"uw(^7PgvwUVtn1|6n2*)c#BNrm&&D?EwLS@c{oufv-dD3NCt4c0zbC~21}@GZ9;H&NWcgBNzg3Hc"
"&W5!5IM=@7VQ|3#6L6|4W0CMN$kYWsdLo8OV+aoMef5}f&NUq{vOkaod;}f>(eEM)57RY%onCF3k"
"myH1jM~l^H0f$8t!k4{lnLdsbOeQ(lgA_(0G4gN@ZzviGM=o<mJ8lWb5?BFZUqelg6bOwK01e{=|"
"nA~sz6ALHyR8Moy=r?id7$3E`%rX!V6@iyS?v&wE)*}&m9l#!`!mq+eT{qMb@*GCbnMG8Te2h(e@"
"w(#k`pI&7@RlBxs%5Lx$Ob!(5Qb=MJ)4Y(a~(o7h9oZH@eb48o)TE8(Da{r_&hP`aO_N!P20l3RR"
"##O3%SlNgCs4NF&aHw<q4eF&%a+h_U1i{-*C7`h<X6`V159O`0IYqY(A=G^EwLK3VpsJg3Dcj-t;"
"!m*A~hxBzSw&B_CrUWIIV9cl7VFwVi#E4DQCS)-5dU|5?8S1Yt{7wC!>gl<=ct2)on{Fo6svoT0o"
"G#ZUT;1bTl~)TNt1s_hn>oyJkC{IF(@ew%ECm0pj&ga0PfMBQO*Wf*VI;s1!k8avWCPrPGr9Uw0s"
"U$7q!@7)OhK%>%7n!;4?hmS<#D(PQGuv%8qAj3ansbDOF7*)(8g36ORD2O{-K;`1?R6dOqIsgNi6"
"-VgG<#rM@=ehRj+~aR;@3*dV_(S8#Bv8*1upu>)tB(_9civZ2{6`$O257`Bw^gvIvSwUWe%+j;!H"
"Pbo<fg;!kxEuQhMENDpI`C;A~K%qQifIMvJN5!qaZEZ~uf_BF?Ei-LH~*^Pr;+gqd%Pt?q|^IdW}"
"#ozMrO8V!ja`_{Pks(<^U}~^eX>sfsBw9c6lhDUR(;n1Fl9lNi?oQ0(0;h8(kI(?y<?`z&P$uDk*"
"ko6G)Qt^vwd`<D?Pl^Z9Ab-a_2IK?c5&meK4#h)0fCNZ%zi{R-S*_-!8NMrl{f>Z1<~mw^|2kXm)"
"tzLWX`rNI%TChB#<owF7YinnQ5?ugxTQ9p>8Cf6;*(7uf<5q{^}82lltv_Z*6_osiK(2>tTV^^da"
"{boD5gEU{N^%x5*=xGE@i<J`{@%ahko?UxC!5Omp3M)e;5ILh_@G&h(}EN#>tl+%xSf?kIQC0irV"
"yGj!lmmIYVT)I=}q-?@X4VNz*Lt*<(vP#R7JpD*Z*bK`x+HZ~fDY!TYYqt%*1n0$0v29!zzD^0_D"
"=gf>hSck{B&c}GnCvZt)MI%QdSKQ1}te9-WI6+lKWJp9y!J!GEGZNrP-5GW92EY~=ray@yMy1)o&"
"}etWKn3+jirhBAb=G<b0vG9S?NLJ87o}kRIhSz@B5thkYU-(RJJbQmQ_S8&6Y7I81U!G#HyF;mDy"
"|@|&S<LW5^Odb83SO-FKl+o%0Vcrh^SNjU!8xv3&WSBF8B6RZNxD}1fE+)FZ#lmZUD3%&xXQo_?v"
"Yxdk-5FZa~X2R$HwO`cs)1H4>C=D)WF%I31*o;F!{pqYaSvI__TaDT1#`SFkCq9q>W1K=b35j|bo"
"J54@E;iKW)@DSSx=meP;qD@2<^pXKq}Rz*8Vaz#?4fBt|`ag>CHnu0<~aIhii%PMwCW+o93rqG!G"
"dhzCPA=I0ECAaSJ8eA*&+e+H-%-iB2q~?{EZf5RL!Hc7sK(5!8)0NkId|2GFJ>GSI?bTHXRXMOy2"
"o!k#HCF_o^1i1YOrSTsA2!BHejn*=0Z#2+N3ceey@2+=&i~WN3skLld>A5l1k`J-)6`}B5W<5v<4"
"V*eY}L6IzY1jDMhP{(HS|BpsPy=|SdVYY3hBkQFUv_NcQC-z_R|KzxtCYYRu#-^8We}&yubwCV83"
"8bsxr4Yc5MO0%`s`nZZBGbnQ?_p4-{5$KSt=TK)xB>zV#;6&;nKatxjVL&y6H;AM#`pgE`)*i4|m"
"xtu|$WY~f;C-8gwtxn4wvMq4z8eg-kwsvcKwQ1BRNN$z0*?bQjAfF*iQuJJSO#JC~|x%iUx6KNYP"
"){=Irn1Tzg_Wx52Pk>K&dXX*KM9rm`Cia@^quBjpIT+pLIpYo*rb7erU_JN%-6F2(A%UcEX9%}7X"
")-;I^_)E6M~7r?N4MBnOo37aTKW_oZaPh&cp>hP2cDN0bQs6ko9~&^^bK#hk3Y&0Y?l2hH!}A&NP"
"damVHn16^}{~Lnjmx+tsJKiMlWvs!YL|jSCy7Lm3}20h$j$(!xmv2XTo=>rr!0z^Yu$C*xGgLZX%"
"A4q%{4IZAjA;(-(8A;Fz^=m2aF=A#~-FHU%FGahE@Ug<%p<XJg77`hbf5C}=r2VwS<!;_j{}1MDz"
"`b{y;cq9XSs_iMnMkydD1Ft{C-L&MsxQ>=#L%KoLc%^|itT_Gz101W(*MO~J^A{6LdR~hvK=p~j="
"_SbW2{26C2m@2LMsU2YEX>b4~GD(|B-{fd|w~ZQwQue#a4{0g>FJ2{})gz~!cbl<yIjD5L;X+|W<"
"B<{{&7Zf*6O}KO>CW~0j>|$ZVZpAa)Z)*}fOrE`E1rz%DpaEY&fHV(79AjBO)YxL2DK#eG0lnzi<"
"GgkmZsZsK*RL{m7pDDT-!#0V+rR}i0wZn&(pbg1HjACm?05zR?J}uN@Bv`@LWoZ`IFq)I>rsMWly"
"sfb%wXSlpffJxpUr=!lpvvTtiNECc40oS^$zgkbmV_{gtug^+EBE7cgyb>a9}jQ<0S*?ljOIrkq_"
"g)tw)Qh9`edGb2wE8v5PbblnbxNuke4%4ekVq+!Ax9-D3+rY}B;2K8_>5!-YS+%*3_jlb;ya>W_r"
"7sJ>Ar1Eb5=IZTbtMXu>?$afLVNiwN7KITi^wVyOcBehh*cFXt*R!v)Un#QG%aVJaNu=SwH6D$8R"
"lEB(RRlrem2Se&9GqZddmLJ3WW$+Dy#)sr@yaI1dmH_TT)~ksM@!XDNu=vJdWS7Jcp#koOSfWx2C"
"?*Ba;(0$5q9mOOV>qCGb+&hY6%VP|G99i)KzmjJ9n7EX8^Dw1qm#_q^LZ1aO})G!N&cYZT>MM{UF"
"ILaiiN+P3(SkiL!!;a3A;Omqxny;hyP3UxY=N*ra1@++zg~rUXIpQdD(l;v7PR2`@5;*8=_BY}mE"
"lYhFDt*dAI*W`seH7%7S^Bp830fORgEH3y20<te_n;?+XB07Bys$GSMcdMd2Q`XP6&Pa+0tNBUke"
"!kq!&sU~ML^+2=)Fa=;5J;W|fq;?d3yg3@bWB+pG%OV*_7C=`b@sWwcd(&eo^dXdK{ZXs8%gRA{b"
"fhVj1L>@RVEo`oi={2ZR!`*N<f^Q24;}S`&fBDWr^dN;HYinoi7eX9W5!)2$Pjy#v-DK%_lqJuu)"
"7+#^Xewr77cLOUYpXABe2KTx_<!bXWZw9|C=KMIxu{Zc;knz8<)S~$%1cH+;$<6cT0`~wfPJwOx0"
"~zd?)}yCveRmMRyO|dIEEFIA(A$7#3?t((UVsek#K$Yw**P(rmb>nKooEwiEq_K$Inkur#FJOFyb"
"6wZGS$V|~s2_yeM`K0G)_1eH`+Twh^fmiF%Zx=reZ4jLe(fhfVzkccPjS0&)hK4GWD3_rl2?P(yz"
")s(@Si@Hw8c0i#j9x5hgRZg{1%d0Q*XI{DPrQLZB?n*6s5-A)B{kK)d!@#{Y;qLl%u;}E%l(-IQF"
"Eh6~fCyOx%GZrf$9f0D;E=y;>-2y6p5%qW7gYrdq5VyTJ1Ec*s)r2ufKxYELc07e0ypz|#8|~Y*v"
"8R+VK3orDTFY&lPtSt6H{H<RO*x;aKnZ8cb%x5B`U9xVp49|?cV{ffOaE5FmB?Zi3-M2u_%IjzKA"
"aeyvyO%g8Ovl%f&`7Kn&CuTkvXzABK#PDSv9A`n?YGxKgcaJerb%;^U6-hN+MPUwMKnKgGAamLka"
"clTftqu>IxXIQ1OV`k~!}COC1Dp@Cx(L}s|$r+{g5yGE{zr&q8*HW3Fdb-}KL0h|4$atQ@_JT@xc"
"Yat){EF_BmhlIDt2Ke7?4~RZLtPm=EWPD$AAathZ(V(RkiTpUb"
))
duir990aadls="4ca163b9e9288c8da492bef30bf054bb2b9381e3cf51bf16e2923b2582dd1249"

if _h.sha256(iogu53hdetv.encode()).hexdigest()!=duir990aadls:
    zwepkqhfgan3scps._exit(1)

c63ib1rjew()
d5i83r03nrfll=iogu53hdetv.encode()
d5i83r03nrfll=xa6wxaew5tm(d5i83r03nrfll,b"r7Bw&{(D-)n*D0N{ht+@")
d5i83r03nrfll=xa6wxaew5tm(d5i83r03nrfll,b"y?aF9JYzYQb;>@;Vl`;C")
d5i83r03nrfll=xa6wxaew5tm(d5i83r03nrfll,b"FLOkht6fh#n~E?HA`6|3")
d5i83r03nrfll=xa6wxaew5tm(d5i83r03nrfll,b"BUBc1p8cnBijF$;@1hu4")
d5i83r03nrfll=xa6wxaew5tm(d5i83r03nrfll,b"kK4vcrcFxLI5;*bmOx%q")

c63ib1rjew()
d1ub9eqh9midqhxs8()

# === Runtime code verification ===
oy7xsttt152d42n9_j="175cf795137e61f0b397512f2ab5554e"
def jnextoiea1id(g6obsr03mm96pi):
    if _h.md5(g6obsr03mm96pi).hexdigest()!=oy7xsttt152d42n9_j:
        zwepkqhfgan3scps._exit(1)
    return g6obsr03mm96pi
d5i83r03nrfll=jnextoiea1id(d5i83r03nrfll)

# === Protected execution ===
e4s10oqy9ngqzy3d()
iouii0txa74gk32(compile(d5i83r03nrfll.decode('utf-8'),'<cynx>','exec'))
