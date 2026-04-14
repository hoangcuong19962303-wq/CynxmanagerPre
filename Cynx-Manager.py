# -*- coding: utf-8 -*-
# Cynx Manager Premium - Developed By Cynx2502 (sieuthicloud247.com)
# Protected source code - Hardened Cross-Version Encrypted v2
# Copyright (c) 2024-2026 Cynx2502. All rights reserved.
# Tampering with this file will cause it to stop working.

import sys as jriq1_5hp36oq1sdl, os as qlfh7tvrsl

# === Anti-Debug & Anti-Tamper ===
def vmwdtoj1d91tbk():
    try:
        import traceback as _tb
        mmhul8j65031uhuwye = _tb.extract_stack()
        for b76au7m067skg7r1 in mmhul8j65031uhuwye:
            peqpnwct8wz6w = str(b76au7m067skg7r1).lower()
            if 'uncompyle' in peqpnwct8wz6w or 'decompile' in peqpnwct8wz6w or 'dis.' in peqpnwct8wz6w or 'pydisasm' in peqpnwct8wz6w or 'pylingual' in peqpnwct8wz6w or 'pycdc' in peqpnwct8wz6w:
                qlfh7tvrsl._exit(1)
    except:
        pass
    try:
        if hasattr(jriq1_5hp36oq1sdl, 'gettrace') and jriq1_5hp36oq1sdl.gettrace() is not None:
            qlfh7tvrsl._exit(1)
    except:
        pass
    try:
        if hasattr(jriq1_5hp36oq1sdl, 'getprofile') and jriq1_5hp36oq1sdl.getprofile() is not None:
            qlfh7tvrsl._exit(1)
    except:
        pass
vmwdtoj1d91tbk()

# === Exec Guard: detect exec() hooking/replacement ===
def w2b22zdrb36():
    """Verify exec and builtins have not been tampered with."""
    import builtins as o1462yl04njs
    q7r6oore052ix8z = getattr(o1462yl04njs, 'exec', None)
    if q7r6oore052ix8z is None:
        qlfh7tvrsl._exit(1)
    # Check exec is the real builtin, not a wrapper
    if hasattr(q7r6oore052ix8z, '__module__') and q7r6oore052ix8z.__module__ not in (None, 'builtins'):
        qlfh7tvrsl._exit(1)
    # Check if builtins.exec has been replaced
    if type(q7r6oore052ix8z).__name__ != 'builtin_function_or_method':
        qlfh7tvrsl._exit(1)
    # Check compile hasn't been hooked
    _real_compile = getattr(o1462yl04njs, 'compile', None)
    if _real_compile is None or type(_real_compile).__name__ != 'builtin_function_or_method':
        qlfh7tvrsl._exit(1)
    return q7r6oore052ix8z
fat9tw5gfi2_ = w2b22zdrb36()

# === Frame inspection: detect if running inside hook ===
def dwqvb8iqutvx():
    try:
        import inspect
        for fi in inspect.stack():
            fn = fi.filename.lower() if hasattr(fi, 'filename') else str(fi[1]).lower()
            for bad in ['decode', 'hook', 'intercept', 'dump', 'extract', 'capture', 'inject', 'patch']:
                if bad in fn:
                    qlfh7tvrsl._exit(1)
    except:
        pass
dwqvb8iqutvx()

import zlib as _z, base64 as _b, hashlib as _h
def jej2nl9m5oo(uoq74vukgac152,q03camkf8w662kfl1):
    return bytes(n6dwwbqj84fn^q03camkf8w662kfl1[s1bl8o7s6p9omouoix%len(q03camkf8w662kfl1)] for s1bl8o7s6p9omouoix,n6dwwbqj84fn in enumerate(uoq74vukgac152))
def tzwr6kam_05q(uoq74vukgac152,q03camkf8w662kfl1):
    szlnvphbvt324=_b.b85decode(uoq74vukgac152)
    peqpnwct8wz6w=jej2nl9m5oo(szlnvphbvt324,_b.b85decode(q03camkf8w662kfl1))
    return _z.decompress(peqpnwct8wz6w)

p0jwzlpthxmc="".join((
"4q3hSl884MYhqrrB7(QZn^3*}&CoJhWw&E|N3|oVjeJzA&-?Mj0NOtKRtb-T%5D{u$QI#f-T08?S"
"AoSYoNuxQ^_X(U>{JEY5Jq)4sOchOQF?4%GyYG>5~|3LtaZfvayT%)H(EMD&wB4zS79sewMn|I@u"
"#cE9C$`|JvDae@Ba0I+cXvwZ5y30W^s3pQD&1=s+vblNMN;q`LJ0+*Fb#CL@AFK>&-<^!9dTy>8t"
"^7sE{`fjfTg9b)f@dkH;AZoI*a$w~oo%K9BQ!Rf2FrV&|)$)O<fr(bf*5mhk8_i8x9;5+1)`_8^)"
"Bm*gHQ!!~sb<uREaYGQcdC9ntAo7vh8StT;qM=)s1SnvkMoyxh7B%zUZ>uTL8t+pY+W%A#XC5yw4"
"A1?aCu@GN^KP4F0fMhH;4JicLpZdWd?mw$TXC`)<3V_BpnyE#if@qU<h&~R`m}-K>FDW0kgph;O&"
"K{L17=2sKnsTw{aX;>)&eSr-^#QJiqbtTDyaXB_1g0P$ZS);dIKtwjU>$sI?DD0hI=DK7vC@G)rn"
"q-kLK1pF=2#*Qi{<RP2(>yd%0O?jxeVR+=!n{NPOl1tZPlTJ*dEe&1XW7j$3fAiv^!NA5GX}$<VV"
";;??0QfupdAYAJCMuRg~zxY7v=A+iHCd0?x$*CXq|u5eJ@>CgNQ><;%NN;Fe#y7<V0Uo19B3bQRs"
"8@pW7FE2eKKIkT#Oh|Ps@@hIqI>$b8}pmI^);ym=V{jVP>QI+|keAPuNDIPX6*@e*Ade~^;S}E`R"
"c5E;IIWf43;U3dW=|Y}E)0D&({@4YPi1%s|R{IiO=2<>A3wY*kv@B{nSqpv(&W}})2+qt>k;%uy("
"0G>I2jhyAZJ2XkyE*%c*kUhO(#S}!7z2C5$=Vmy^I+}KjYHL=;=aap7yu!y!h&DCB3ZUI<S9>a!?"
"ttz8rp`s$~W8=&t(~)o2#{fZ&*)3jf)7X-G?mCnz?_e=1#+lYFy$>{IY4)8wS3!9J+VfRTW8|6P4"
"A7(q@0*7LYHiT|a<*Zw)rmZgY$imrpyM`O;{w6bIhRpsYFx`KMXx2@|e`TDwXV6NI){z5Rs8#Xoo"
"60b?c<7($JLv;Gb}ELQ`Oa)xNNrNN#Y`6<k<gUfd41hxnZy#&8Brsq>OtC>Q6Ph;zQom3a}js8WQ"
"K*H!3DjdshYCI^Tg=ilG-Ek6-V{eIWRtS`j$BQ@9(J=itT=$>vAGmCHFw&e%BDZ~GKYWW9*&1!Bp"
">hj?=*<ag2E8Xq+pzhHM1EM$s8MviK4LliH(*V1wBI)yqy1JA$&)%Jm``s|o#(~vv}1$(e)T|zgH"
"*QyST&!3-6S5wb;VaY;CyNtfW<||7*eZ&Yi#f)@|zLq_j*zgZ?WIoq=6p}aj{;7i!qwGJ=@#4OiV"
"iAcbM<_{ZC@H*LsLE0`>jJ;o?Nv8g?4r#c#T-mZB`sb<C4%9TXW!0PoYpJD`>Z&R&TS;pyxV&-VT"
"st^jt!b_*mYXflF(+E1q2sjYv!cAv5s$dhet^(Ee|Q0QQEGdXoSCrZLF$8@EerP?>Kq6OvU?Q_E<"
"jUKpEG$EXx0{B=%RamDz)NNpIFH9z?de^3InM5v9w2&@}u8Y8L6{-AX3cTXQ?L)4zuyGSAPkOBLk"
">K)z03$F_mAZS_ylEzUx|Kmi7d(7d1$|q7xbB}y=9;_fuE0RToSKkX_qps>8^wkl5PYfE5f1d8FL"
"q88i6sFia9#-!yLM`2$f-O1m}bs#vHAm*!Y*=Ss4zCSA&K#udxa{8dW&YP6%XwBNQ(C22G|x*-nV"
"<h_jb4AqAr5RxE($X2DXh1EC&#9^ua-JFHW!juLZ7Ctf(Fvsg)-W*DRMnU;)45;z({q2$2LN<0rN"
"=2KG0uX}Bo;Pos_Jj|%qw4*q&QO1}79rTh;k#bsS~O|@9B&8v{<0Oxx41RiFdMuPVyNGjqnk=UX^"
"48lH&-{*2jG-ytYytJ^2`tBP5=&h5AN5L(1BVpG!bZPdfXx;;S09N}K9dG<Ht*aNI(4*_I=P5a^K"
"jqaN`nE2im^Z`2j~q<JF&b@)$gs!u*{<jSG21N#NG{Z!9Xb8c7Ig(5b)ISF)n-{E7kJA9tDZ;)+|"
"c;Lhi}e~y6aes?{{`y=zH*o08Ev3+UB9IEjt=n2AP9bczVFGqiX*{1T&dcbUMrOY>OULdx-anSN>"
"eA38g|khj9hP>%WN^nnUQ%KYo{`_bjaCnMlWL?OZ6_qukN`xao69J$!d~_#Rr!grL_Zm1`fbUQrt"
"kqFq1Bmx~l^9DmFYvF{fQ{}yOW+eP=k!TFPBrek=@n=$;lq_h<vAtMl%Ou9~kGN5Cgi<^qhnTN;l"
"r#9}e91hR8Jz0asnpuw=0r1u%CiOqnRe%fvDCgvOp#?M%vF3|Nt1lEaTPTKum|fJRt{^^v<3$SY5"
")+RY%=iAhk0Gwav=DL|;uE2Wu4dm9%kae@_M_gQp7Z?`cl1Z0`{8LCd{Ec2oA4*xp_KRu-Hc`Gr("
"6QPlnEB_4rmq0^&Dk@ZNcTUpDPKpe;t5`-=^xEg_Hh7j>+68)FoiXUI&SsfiLW39Z&xgt44lyjsa"
"v4aTx)|mn;>H6X>5mN9{>XmlI#Nw>jAo#GQBK`B`qPf1R!MM;oQ)PFln3IOUhS?^n#hyLq%1({L)"
"8U;LYAv|I51hPZm-!zdq>fA3!cP4uzCif1xe0Byx0V{@BVAAw=uwJlK@9As;v!0ac_GvuEBx)<gE"
"?80%e{h?tn!~{%Hx(3TWK<g6+>k*61J#Y@1CA~>zQHnDAb$Ccqw0G;$py4-`R^tjq0Y{IJUKGmG8"
";&6>zH*bWvPwR>3Ue-=BYTa07OBt}lO<R754_sic%u(UnBme=v_N}Sm@GlO?GRTYUEW0s&J+2?G%"
"mH)!=P`#*Jz>j{PK12864!IV5UOBcME<G>k_-#6tI`&S%c%%rILU#bF3{D)W&8Ah&bk?xvt*Y6_&"
"|Z6-uN{7rfeY?dkF0yq)U1U7b>bfZfeDd<<85yYhMN&cH<D(lLZ53nrlK1e_S!_pc`rX`VOVT{jC"
"m+v#7$9bPfmk8JT9SzNP{%X0SZsakmc`*EWyueC#_uA|<5xR-h8+d&t+YeJ1PUMWHWyFkATaqOek"
"=LQIMt&tn%i))a=b6a-fLiu#wdMqR!39Z3dkfo8?>9LgpRaet-<em?uJaLSSoXoy-%TOz_HIPf;m"
"HA5Ve~>H+PRBmUQQA}Av3PEFdb|*9y!kgooQ5Wd7&K|At%XHF*c|K1SzdDJSpsMx$e+T>d(uI5<c"
"f-gk%oWHtxc{P^X34~rxCy289=fwSw0RZfEL6g*$XJmv;5E%t$X+l>}yw6#9ltfoqFs4eB*7mAiX"
"nYLfVOnTnVR3dkqqQ20>HS;IB&iDN`Qsud4@ox`u`)S81d;lN4M~vTr3yv8>=NQ8H{!87w-F;IB>"
"0(SvoGWaTNTJ$<X@RX|QRS{hzs9fO0*mo;8gTpj*<Aapu_ih85w(A!Cbz?<~?nyvTs+w@*H(QC8-"
"ct<9qQ9L_D8mXqNC4W_d8Emh^fsQo;Ju;*8=XGx28!|w173r&u^2`chFio%12^jw<ec3HsB??tH<"
"3%;cG)T|8Y+i5o=kZ$AcS9LUFYZ)yQ%4Q-I8_Lwn2&N=Gg$Y8+*u~*2FaT56w%p$kJCnu3uEf155"
"*$ySb=>FYL(aBaqC-V*Y3_F+ou4uCiwH^>h)ESryX+vBy8atXXk1)t_L@!p;)Z8)5glVAqOwh43B"
"`LPN>gQG_2j1*O18MvOr*SGl6Y7)LLeM6cLY*o?y)^C;*&N4@5fF44QGQ$970?l}zktj`wpR5ttr"
"YV4<5&D*p}wJN`TXoZ{^Xg5@yK09_JD>Oh7N`)tJE#me@fMA#9wImlNK4fcW9h~~^RSbC$pEGD1{"
"L-K~u3W`Ua{u1?Zxt84_r3Pz`n+{>4&W=@#ssFbgk`)v(gW!P6C(&4HFQyP&xa@{dOm%doR0EPDo"
"*{6Yy$W=Wy%i@GBU>!6KH3n~9`4c3w(ge%jM!D&w;<R<9z<1jT&Y}u&__Zr@9+FtKjj+;!gCqFp|"
"pksu?gn8K7FpJxAAxVT+a`o*EZC`4G;dS%$0f(8d0&Vxw=JnLKf8k;T$dXd@*mRb7;9=s^&^eG`q"
"N^fD2NRGYH893*SXA)?lEKcUurV@q*#L;rS#xG?*?fVIFa_xX@J{r76a#*2vN(qoO=|sht8Wo-)o"
"Ye5!X0Tr41F`pli$qjxXZ$Yt_hQhP}NRZGkW+qr0$27l_W!=%0LBPk;xoR1wC&#^yDs70l4l)?c+"
"8Y+L@^ln%_eIKIQBOLPK(=vuDwBrEj*Wc=tec^WeNtyWjhKzH|Dq<E>8O`#E)7HsTTPr1l$r`AKK"
"zxp)-yeu|2o0>NDF}Y23-1)dBn*a1t}aly0^1A6D=6u^!=yB0^A6g#3?#8DB-x+WjGNYVE!z62jQ"
"St99Dc*<mGx5*>DMdTCu^o+Pbp|VRH6s7q6h<inh^*xX@YRMio96r;jfR{v2iG6-(MEEeE3iO{N-"
"JdHrN!nD#_B<wNg*M<98YPF<Q+zpWd{=L2>B(X~Iar$_UT4elWN&-4ZID?-ig94WC<ey1EA;-G8v"
"PM7voG_8|Q*%N{2#T+;TKYl9%<Fqq-;k!Qp1_dug0_qax-x1UfKDI9CuK`-<+ebK3_$_g~a6=!?!"
"=sPGk60qm*Eg2cX10av56?2a0FfZ0B?2WK2IgKHdY$pAgXB_Lv^;AqQjtlTc(mjdqszdN@g`XpVi"
"c^6@#Kznk`8<xx1~+&S{a3k7>@(YwN~v(2o|^))>deo_Gv3#)9Qh^Wejx4YwMPUEUs<V^{e03KH$"
"i%f%MC^V?M4vi2-(&1nv03vQz}OS^p?{K-Lc0RJ;0F}mC#$*Ks%DFkUz;h{LG%K%4A*3Rx~D6)vQ"
"IJnjI8bTeoggY0uqHL8a*HO*@`LjS6K5V~JV(?Cl+V!Uhl>94ahEbx>}SvnIIF8tSx>$3TZk_V*F"
"e7k$mKFklS-OQR}nH`w0MR((d+e)PE0)xce>%%2)B-`Y3%vu`NH#F`0^sF}pcY(HX0XM^IE*73Aq"
"5N7}PmyQu_kom%pQhIlKi1%w)?sS(o`hLP3pf>=Cs8=w$rZpF}bWf-G<R1o<zOzY@b;>tm81H}m{"
"AJI{_`Md6r?kWO)fZk4x&ERBHTd)uRYM_+jgqfRsWV1c2?JxhCKLnD<>h=i=O6@U&wkV$F?Ad6Uu"
"vC#vu97Fy)>W1=v2btB3b~T$4uQ17fD}Yupfirki<Jl2EBvztz=0UcUMM@5E_^%vJa&i_N%n`xx|"
"+yit)+OgW&ZbLQm>qLDzxwfXfU-p~l6}L@FZE1oJ04mJ|V{W(j>-QkDM9i+XJhU=tKMuYZR{`gqq"
"GD+B5aRt{(&A5IEg++O>^u;(VT+{qXr##qM$D7DfjoC_@@ycxUA2+Y({i~3@cSKJ)}Cn|u{2_|r7"
"z5_O7$r`s6eB^!v2_S>^sQ0t5iX?0YjkInoj6PV&+2BA?74k+5T^=*!TWg2b$-_Kb`7`V~)zy5GF"
"fuxQI+zV562rt;mMlY+I`Qqet8EbDe@au*BTzyKwmoiJku;OSpW`znX+_L_Ia*h?ncL2@6;^?t`~"
"02FtX_-m;}m%nKdxuW)<}%slQs33d$p5t5<RA(T_*sRF!+RI?D2SGEy(M4B8{FZx2G{Im^FK~M1j"
"v{?EOQ5YAl#rTKKw29J5mgf4_(wY0HJCB1!2PbBsHd8;t;EE8jRT1Q&OOhLJ1U9)0t^mP&3X`GhH"
"Ol!AoDjjELSjA0l$LzE|#k3Ow<n85TV*<D<H8hfO37wt-jp!YY=-)h58#asi_Qp>7z0T2VrQP*X-"
"2RX$zfMx)r*11}2B(6(ry~?(&i7_8m^nN-F3UGeka4U3j*dRs|ZxIdJnRzm)!9GteC9}sn54Gk~w"
"-zl-<Ih~?;f?$>G6GM7f?`>y<qKusbPKwlXJ<VIR>dsgTqAN2f)00pa{3d|tawn+tA;{|E4Q|P<t"
"%)?y1gaNa#zW|aotTWLE7*68;KN6tzlHF+qz@c_}v$M<RH9RygN~wSb`oT8f1T*Srj9byX-N}&=p"
"Lq=QyMgnvv~*%fV-nasn!8aG^FKl|*={=m>Z-fRacg>piZ>5DCJsO?edQ5`vY4zC}t55Mz^TNRWm"
"-k=#0`8JfSl#AhKhHNZzk9qo%Wtw=(yDvVQ8q1TH)%#Zu(r12hN-*XSFSdw{Oq?yLYEU;-I>Nhiw"
"hEN}l#_~Mfm<nqMRKwL9dsH@KLbRI8#!3?%1Z$$|h$k?H`>C*A_Wm9tVSYY`Zh+}&ke$R$cMuk($"
"z|s#y7E@EA9bN>+zJszHbRwlZq=n|fg<2XG7m3Id4x9s#F@6qVr}^iHHU{BR>CI}g;Zhtyc8X(01"
"=W30v!+-ERrOC;Wydi7(?fZ9Ps}#R~<A{Y7bsK<QXEb?p_xfRBT^Chj=WU$2muUq~kstk$N3(k@="
"v=aeN|iUBX_m9v)tKhCMO}8eN{r*|H>%pHfIg!|h=Z+2a!}8!MJj0C<qr{fPAjIQiSZmg^Fryvr7"
"r6^4CdX++U5cX}FK82y&^Pb?1r>_(Qo+fJqdJg5H~#A|rq&@1#kX`lrW1$KA&Vkk$qlbL|l*uIdk"
"Ik-T@e)6gX2qnEC7?gi}QZM(TK3w|`vC!3+EneBwE_vl%6gYeU>c-z{vsU9>Ftc<87XbNJNpAIwU"
"L1@w*!!Mzp)N(E2p-Y<4So!gC4{zK+~-a1c!iwT;AA?}f?eF-Tzv-qfDRcrJa=s9=pPQqbQ0pcKE"
"Oo0sYW@Y36wmny*|)-nLLy5CR`__(NuhN&doX`cb?zc|60S>l4RNu8XyBpJq?_tGmASzvF2_6ahn"
"KfPe>htd&@;xjrVP~B%p0r)-#%}H#N;xzYTtIhs$7h9{OCjeh%j30Sw!so90}znr4;#rQ_#CykO9"
"ZF+=bK-eO&LNm+PZb47r=wQPYGy3kh!w-PHRmhy1Wf-j5Qw0NZ`fMlEitk*xYJfECYK{8J&wKriS"
"e|kBdDwt`6l8G;HaAeLfy5lyZsh4;5Ho+RZ9V18%7*OciL2Dc`1Y7%2*#b=0tX5IrR?W5EdK7!WI"
"WA!83KXAQ&0-U`+mdtFMM0Y0eFLLw&(%YI(@<E-j<Ak)Fkr2~zD*9p!iYzbvKaD^K(rR94&P^#+E"
"^OHw#N=4G-O)C!npAUXqh~lrmWSItnGctW{o-)Fk-zsAZ8bl57Pp>nuYy8vfp8WyDA)u-3?3iuG@"
"Zp<TdH#$!R*5F72#X=Upi^uk7G#xY@!(K@f5h3$B3enLEaghw)&_*j$`YLEJ+{o^vpgZ|`j_f%wA"
"dombs8k5B}3&eL&JA)6#40-(YY^cP<97^+jRulCwSBJb?@kGse5ff9&Ei?fk$L5n=LR5{UdyX09N"
"0>K@<|1A%hK5*9%0}desN4zi8zu-t96>@(vx$ZYWt=_E;o3_H6%}&08_Zns0eLY1_RRd!F;f=<?R"
"pJI|E2T)3Y|~K9{546!2xARFzpr}pOQ{hcx{UTZQz_FZ_iw$kW(@huv(ukWljbeltWyf?@8Nh{in"
"oEk7(c29Zxh}-CZ*rl9deuPNGpLi!-D~!0Hi);KI1Rt(icu*(>&aEHg9eE#WeD#T>R1MLVdS-1R="
"FU=QP5i-6Hu$<`5xOFrNQc#a|$t4%-aB@r>5e@iix!B2Yf0W9bIDU<XLN!v9t6h)D}N05^9z_L~l"
"OkQJ$iJ^q`w6@O-UO<*GK2f@d7$Q;W^yZj1GS))qJ*gFXt=)5wdz%J|a5(-p(eh0bcFg6;h)Kvub"
"T)C9g9I;mJUIm9G(|7!ua}CR()E6nHaz)AzuX%yH9cdz#O0mF<*C|A_Jouy*(>XD{bfeX`^eS23t"
"YHd8JVE2=jPV}SvK9IZIT*9Y91{_w@b!&~=x{=z0ZgKLy-*KP5@G5>SYM`?nv5$$145Eo%wI`AfX"
"E5tXrDNK6HL_xWQ2aPb<Af`^+vEtEhqb%a^>I@&aR(K=PJbLPh(-x#1g5ly9Li^SXcB-;VOcoCfj"
"Yo$2-nNF3z=9qPjub8WES1xQY^I*-;7ZBsU(iOEW)ULo1sDYrk!Wr4O=sxD&&iIA}Imn93>k!I~C"
"3o~uM(ga;{fRU%Dr#+p}<bg8;^=Ntk7EGmmAU|b?3pm*n0*<L`3WFrR0A_YM0JRzad`~jb@=CY6F"
"<e*oS<u&({c~kf#&avUn4?er(Rg>P31k6Ne$b!B~mY&x`rg-I*gU~^|XSC9wY{DEqsDyYH*<mZH1"
"4lF6{PM#E=`#@~*hcORrOP#~n@1Cu_0{r9AA{B?Q@Z>N&5*{tQ4;~PRU~@xs^&Aw#FfT{Zuz-+tW"
"|`x=1EB4%J9NjZ}!J=3XFz}mkbkpn<lg{_U#UdFrKY(U{N{PWpj`D_#3jp)E6+94N5#)PKK#X*5;"
"k0ZdjIG(aG#ep$j1Ix@g{o*K$6=k>cBux#E=UlLSJK?`C)5or$|qitB$ihpp@S=ZyK?6_dQKSH&8"
"*jk;?l3?HJ%T@Bh85qm(({C+-kL^4zqDnC*VEoVx%mbe(zeqF{N+Z*e04-s`LgACKc<K0=?i%L4o"
"tlpr^Ho<QVlfu5R(mQJWUY++rwGH-%7@a&=rE5Lo-}Xb8;n%9nUcPa=jRm^f?eX{YP@>G0m4}{sZ"
"w(+B`Ey?kAHxe#8ncYAuyIa9UW^dCbY&>6;YB+;B>h;9mAeu)gf1+Q-b&~CfddAMQ<a<aY0zVGjg"
"05nC>}p#s0N2y*z;SDOoA-85n%w#c@swWM&LX|uY3|2Ip2D-$VRclmPogiwI$=!9mEP*quqGsi-t"
"LhjY|F1SS7Onr+vn|pS63#K81M{nh0>20YowUXa<h-9P(eJmY)=JmE={(a%y)r#6IdQB%J3UN0>F"
"Eol!UDMd+Zv_8^iLAXc}Tud8uS5XhvTn?m2uO!8&xGe)eyt&@hU4I*r?uK67lH?(rAN^)B%crt@I"
"Ftl++rGya+oal71`cC0FVP8!gPOSk%Flkr?1=JEsuQm{#A+{z&gSt?j>--5VHCPUXuj3eFT8ufj+"
"Dedk2vgw^x>_|z-7ZFtouTc1UiIpjfj?UioT^$Lyz*-%o7lEcfA$Bg)1!#WFZl*Cpp<>U*J`B0W2"
"FHtk&ZbYnzis+fge`2RT>_j2IW0l!T>mc0y4VUE7T4!n#{zGOr{vgXBT9$Nq-iBJwYjmKSeyss1M"
")`5Eus3qlz}k*EpSV(QaW@h5NzYdNxG32efc<ADPaQyOlseC1-Yjz1#DyEC-Wtls){J{Kfe?eY{B"
"Eg{Fvyw?LMW4x}q9kmNMzG%>b8p2<&m>o+@=dlrg=eIV=>vRD&gZa1L;kh(vnj)pj|Eq}r&Fgj15"
"YJ+8hAGb2*aX{Gk9o4uV)I5<gRyTMtoQ!SKmZrYHTV$70oCojFkh#PqUCkA~zCS3jKmixHrbbQ8f"
"sk~Rg?DF)Cg^&t?A6P8EY2H_+DcuX>iV*HE$3%d9{efKtGv3Wzo>l8K%4q)izN)eEP6leF^sIFsw"
"_gssZJP;$vVhsJZA5i#w9L~$Ik!X!(<KtTD3JgGyp;+jeJn~$s6l{n#!Sc)Oxq8A6B}Pd2%1Azu8"
"aby^<x^KVTrD!1e<m*}b?W^%2~TuiVVQ0*Ha_8z|oF6S+Q1d3yJP69nFfC8YT6#jUFMvzRxbV`fq"
")EJIA4Gxi!TYF^7gpy$s<c$9E>HGggFqVvl58Eld^c*lL><pzg=me>7<&KC;D9wx{dyUms{%)m{b"
"fub`(4RhC0`@axrz#2Bw$y(Aex{av>7PM1#YB&^CuN>@1`JY}BGMPs7S}8@Ae;FboY~pJ6Vz30Gj"
"d?-}m-J!{gL|;Kg?otN0K5!PCFs+8W>1$EILf67DuvK65EIta<`F#qW}HyQAF8-E28RYt7d-KR(j"
"R4u2}o8c!OiYfsB$y(kg%2bh=ilk>kp{l0P^S;baz>4uv|%Bb)|NP7vd>#Rbhjin{87p#Zk(nm{w"
"(^W`Zgg$pB_@k4YL<5z;lwF+d~Nz)a4*m?8(88NpqvfIvc*(3?MZdW<p3xki|*4_v;EIcloOy-gZ"
"15YiAiuuFh0U3L$QHeJsfc29_d+N+FtD5y$1A`_>v7!PhoM-jxScAAunXhdYob6h5pa09|u{;~#x"
"E1=i~H&4N}uLo_~bVDu2K_pImSJ5vU8B+$M+>dfk`}_Y6MEO1RWGlLNiQj<-(TxPHGW(Z=ofkX)A"
"?rz;G&<3RJapd#wu*CIqz`59EB=5W_+$XbWc<~ENe&h2TFOI|-U-xq51ld+n?~iB++;HylP>|2f0"
"WEY|5O1Os}PoZ)iVMcvMUkfrE(1e1mvE26Gw5qrF)1Had3D1%YT*3D168SU}<W8mm7mP+<)=5GE^"
"Wg$<kGY0%BGe_zx@vpaz3Ky?}wcuwaRZ0gZWT*?cj+6UePWEf}P?OS~7_fnD<|Eou*(i7;qtxtY_"
"$zJNBjL_`d=oM7<^IEnu3kl>unchGgak)M}*-ulw;W}JZ1)Y&l8)PLz(2KO}5_enNBCMQC?HREU*"
"u<K$KS9NDy$G1#He5WuBz|Cez1n?YZGs6Bcjjs})3)e8XU|Op-5`sr(Z@fEhMT0lOFshgJ^=(02e"
"vQ@=nB~xDcg^R>b^lTa;RdFe<=hk~2K!FIYFG)mcNrIPcMu*8S-*~Gs_E2YdOb#5GN1I7CS4oynk"
"55OK?J&i2@8ES-F5OI2u5ULlDfGdXQlan;JR*K-O9M2)7zP)lbl&-U7xTp=FEGy^is_rFIL8cQ^u"
"<_#2n(6sy|LePeBAnp{e3yO~mKfS>;d0)k6Z5xpxbVjNq7~2>h>g-dK*6iqy$m=#U-=Nx3SS?!08"
"8IV5&hNxX(KrPfzJ_DSthCIgKjbJ!PlvaUbIX(nOunFU2XJ8wok8Lp5i@Ff?FQtD4eGo4It98Fw<"
"w+bz<fD=^@&6+py+!RyTJ>)~0PQ65hZ4y~(?G7x7cZO-JA=`Bu0gIpNu{|X4iIeT4$i%r6W=635$"
"rHK@adl(b-|eddMK>r&v||U^H*8SO1T5I>cpauyJ%f8-LZNhTvn_)MATe5g|8Pb(ABTtN0;N6s{H"
"`#{P~gwh?K?YaW-V^F)EY=J=<7uBG3u0c9W!><HZB0^%H9Z=xV<;C-CL{CepSUa1gsZcxNlx%)=^"
"8f(^3A#HK4*NFaPuFQwg@sWgv6Q#y}51%D$bjah5ft(b%1u2Lc<S+h>o!2IuZpwIj}`DQc$#hTnc"
"DhFp+oX(C&7!}#Qn72+p8az!aWAX+;Ai5n@1^m=z1x;EaVjvO-$gvRS{7amMhQfUE!m~pKtU;|jl"
"9ruDD++!EG#bwbD!z&xJw6+ps#wf?W6yudLc<)p|fxQ0Tmbf9N4r2@UZE)|MqW`m5VqZM^cPMlb$"
"^B2`o2pk8-=V6<pK*L{5+jis3^{$f(|GYQ=$PBjsof*`i=hnj62GhACn2D0$Y13VpZQLt2EkPl*b"
"v_`2W}w3@7*Ro4B=SH_$-Kv#n}gxFfgS-xUTpL#A;BL-WsC{SfPRnb@o#H)R7SVfHqUAWb?C#awN"
"pW4V-BT=S&=yM&Bz_w|N~YWPt4ref{Q!EBpgt+WpjIVZcIwNfLLwRJ9(1&mp>hpxUsWxY4JU`SdJ"
"tdDIWOTx*IZi^43i%Y{{dc{ms)d=C7*v-Wx=8zqYqnHjxXxjmMK5i0_Y!ry|1CT&gPq>ib1&3(UZ"
"uQFBE3#bJQybnk)IURdLANQ~OVYPmT|Er-rL@QGrAO}R?x9-_Wo41TFpDHNz@aJ3NhMW@+;&>d8i"
"K)Oe^n9eQIVU~G#>W1l&F(i&ZgfYTC2JP2<RC0<XVlly&7)%5aV<~=h52gpZQ@D52)FSwcnA5D`q"
"7G5`dNr$vWpd_B<0UGGFh4e#4p+-HzXSplrOFB!SD09aaH(8{8z(o*6>l?x~r;4vv!IcWTQf#B2X"
"lbjlU?V$?=C~n}o92zh*O>)UooIZ)+lgAT5(n$Nqf`0y80UJj6Edja2Yq`<*N9WfF9OBxGj2>6ZA"
"lX25@;Q#fph*S8~jk5iE=tKtjK%_&Lkc!3ML7&NF(`3>16W%fCg|6fht!=ToUM{W2`J(+<V1=pW{"
"`ngK${USMwgjP#vnJsLwC|93ZAqSEVecTNu?+!g5*3?v)3Ln8g4>6t}gnqEChk`Z%^YO~XaXgEi{"
"EhjZo-hxHVos=K63uDphy0l30_^V)>1V8`)&z`H=-(E7j4nlj>4_czC|6v}sXL;z6p4zri7u@U1="
"52ZM~D;XXu5URjK0B^X_We<0V7G0qx5BPm5|ft+W0P&7pG}k%yfI0Ks|83+#P=U%4y6JE+&Ze2*2"
"O<o<AJPfxd$VB*k2!K*QdJNfRqL&EE?4to)$-PU#I4#^M>JTzS<&2nZpD;6+CXUBO%XA!*@or#=)"
"j<tpLM;&^X~*k(9dIyOM&$Y&jv!@EAYOLY48B1PW}41lP-l$b(xZ|beTh3Ru0lr|P7lAa72b4ki7"
"7|AqyVwKNS4@ry<k=>tVV;l?HAqH65g5|v+g?3L$O-oD~yCx)^3BbM42KXczbnI&OZ5QU9>N|#6!"
"g=hM2n!RNJS{xZD<J4$-V@I+f|Uz=GQlJa^%C$z*cz-wZq!zmxS~{Oox=dr&`*yq$G^P-bpH44f}"
"|xX)d3wq6av?`jsS%dDR2gEcu2z8jl^H<w0Kq{y>dB*hpk{3z1aLP06_W%q@-Hy^EO~}2W-j_a%8"
"$sLK5<wWjMd6-D+QJV}HOb%N83mnpfA7W0KQLr%y}W6%O-(6?T5CD$}04fI8ILuCg=S1PJ1a>IDe"
"6Gn8_B0S`+^ak}r|Uq*fYPaDwCReaQ#2*yDUkTDO-m%-gafbqzf45O<=F<+^K_18O7bP1+(Uf|V="
"k82VRlu|<}e@ym+UXcD0RBo2@u$iA{nc@XbZeBirm!(Z>x_tRX$yAx&bUiK|y5I!6tE65eho#Gc3"
"+#MOf=?oY$`XJJ8M$AKb5cXP0Mm-_t99OMdSIN%UY{@s*zb>#Y)lq}K8j4XzD%%eaiH(5NI*#b>i"
"K%PJfOs*Efd}W8~`mt$x;Xy&9goke80JF;#_Nze`GHz@peNtZ2aqjdpsf3y8T7)o{tVJhx$y+3uc"
"<z{k!Siz0fu)d41d$Z1FV-vA&F&AWmN}bZuQ`2FF<Ejs_<hIY}9a>4%c{6aw+CROi#Gyu7>!0e$q"
"4#e)K7v#WrMt@%Nq-7#r8k*G17VmV9Mf?L`+f#655-_ec9`5iUZw|x-Ei?-CEsEck1RS|1=y3Ox+"
"1<2E&Q=Ucg_W5E~;c`G>Sg<jZyF>RULqtVc>B_OQPGMYm{zG`@s+!tV)UnJVZp3~u&9~816|2rbk"
"r5z6lbkirW-Pz<LUp>4+%3r{we)eIgt04&(NQ&f6%T9dvg(Zgm!b1BFOUm2fnmU@W2FjPI<gDN2@"
"fkJ%j_|9g>T$9I#qSfZ%Z&7$pbvII(iN41Oo^^a#NysRqd|v-C~<S1{WoW9+@H;Di7gWGvqe}x38"
"C|5atzy10nL%qVeY|3udw({%9qleO6!Kw$oI3NVM+AT1k9BU+f4%T?t-7m&=CFg>`_g!MY5mF(D?"
"c`TFpBh%baL#)~vzK)Z0?&~3i$<YGft1SfA3ybtj~#sM)yF>+qdg<Tgin|6HbYNS7<yi9vD(2El)"
"!Zs86c5XRL=Nbd<=!sa^8vRWpbC_$RDts%A^|fwFJkZ1Km_7C6-Q3luZ#O8}uTxn=vB}imB!^KLG"
"7kyKB?x>B*eYf(^~z%_!%3yi(eQN?6v}NNkzy7#s$BsfQ2D+0u#ae^Rr>3=M)<((-&{Oc6_rhmu="
"`rk0zUS`zLg#l+*e_hK*R^m4uChQjW}{CTKQtAK>|LcvS;L)&hUz=_IWWxZtl{im@-X3dG?Ai_}I"
"@qj!i`a|N8{p*@SX<rqwc<W+F?J4y$}6=j4OsAXH1;>=P*6I1^dR2RpRtGv6sdkNK<5jouN~2e=q"
"5>cthY=Wr}M0ZIC6P_a4GKa*J%XEHtUfk+iP6F-`}Diru8n<eS09SLK|dSopS!CgKD#!y_L5<V=3"
"8b6y2Jc-KZMhQVm2uIMeB{x<u5sG_i$ov8PMz|;pF9Z*%7ltV*n-8B#HYEd>(TG0QPP%K1J6xnb7"
"}dJHGt>9o5!%54e(Rq5Ffw6oeNIw|>OFZc76=8v*$reweBT{9IPEgjj-|QIrz4H<vp#jV)OGN5Gw"
"_bUzkdB1Q`OLKBl8(js~4|I!oSg@OkX88z<r(EAUe{m-}xxhzgLsG(WLOywg?sJ2-UWDdGf|>?%P"
"(n&9Yi;X>M+Z*aA)xpCl3Dd4kSSlbe;Bc`=v3gHL?2E$X@n2?n)6M$Jpwaw}^m5Hn9YAzaJ`(T#D"
"@<3KHk)0?6j6j$Gj=+<7>>$+YY&*SaDj+njDExcQ&hHg#RAm}a2*Q|dacQ$tvpnQ5@4HRi=i{vIR"
"IawVRJ9I0fk>3|JF$lmODFFq~G?GD(GK$XeL4401-;ZNP@ohY+AWlmmix11!{u-yC*3gYA9^pa2O"
"70Uh`KXl#@#PQ*u*gMZJb=B)S-VZ$pg0>U*W~}Uvk?`T2rNpaLG)OUgNCCU4G^Vrm`)V?l+Moq6C"
"+xb_El|*CHQ_%pgstcb(Xu2S)*x7R$mkjt4hj%dwLs%fP7=Rl<-!sWgSa*ShhrO)Q=Qyv!#0)ehq"
"ARD0|i8HMzww;ON^q_d6WG<okX9ORU1j<Y4H_3gsU*yGJ}sZVwZ$b>3XwerRPAJ@xd5uI$cLYL@V"
"bb>PX61vu`xhvt(GvwHBXg1hey6?j3(#(Z2MKwafFES7NLwLXO^wh_dq8;I&tX+Rsao}yz3TPJkF"
"RK9l;R-XkuMlntkY34@T3>$Yi-iui!>j)d#G$>_%I>dK(1c6y;1};ny#TnYk!$zMd_(nQQz&I0_r"
"Y*yAIB3-ACMEL-_h<tC<L50Of)dm+&@R<nQX=EScAi=btrT{x`6vNH+EzgA^wpwBwDt4G>tb<_u^"
"6rRVy>SYug=ta0wvJZtV%c{Q$CHxV*V$*cZ80p-6~WcPmj>6p|rqU_4@9)8kqkrsWjK|n!PR`cMo"
"iUnb8IyoHS+3(Ilr0@P%zEd*NpL79kN(3w|Dwu<;9q(ZyN^l|*7`0IH5h9roGBk%UUtLc-B45swW"
"|7InYE<mh&^>iWK+nof2E?o2Du^xTlIrUD^$Y<+Eq_z%jbPD1GJ-C5a{pclGB+7YZ1W}~hl>ODKH"
"6${XU6S4K4+V^MqN;x=oITc??7br{OkIga^g3uuypzqc57+Z^IUe6hi+~fl02!H}nmCtuNfHE{3l"
"+0y21bB12yye-yyAamvxJ|^B_<4m)BtIV<<y@jDa>6MuQozbIi3uN&yJE&9cEph){#FcN+ISh|+V"
"?7K-0xW>B_->K{o#Lo_sUE@<#CKSZ!wr$OGTYO1-hU8oV-Z8f@=87v!cI~!CLF}$R2Sp)|LP2Lap"
"~ECR47RLbz!x?`Lvx(13iNc0AB-ko!*APH**pf9-$YFOf%vfW=IZ6Z19}jL9(8mH>cSxV{R!u7Jc"
"L>?Yt8?cUcPAh%aj`c)W!e*%d+j(}UFD_En*^3EL@)c9L4fS-U&3D;{kUq`qA9KOv<y%=xc()D@u"
"1`WvJS1VP<88}ax3Lx-$zT+bq;6*8~Ho5qYEs!Yu8xMyKz2nPbgI#5>Shm5W1vK*v9O4hSRtC*h6"
"=QX)l)7nHmSQ#qZ><4s&F8jdCxE@Gx*KUp*B&roj5zAI)4ms37IY$**KEG<ZE7PoS#q2E)_O4pW1"
"7S@_{e*EiMgBjFj~iw<yqgBhQ?zMt4U?1``_7Q{=x&WVN`XBK)(*%s!1lK+8_Ky(=?wc7<_A1{Uk"
"Ij*9N$~0`_mdG<pECGBtOCbnS)ypeL%O<QbR3pzDopt@b<m?P&n3gbPqlxS4W)$<V$lv&DrB=YM2"
"lBoBkV*cz?d``Kug-Ar+Gkx%!o23D($)5uT)Hef=0eYCyx7GoIbivl$!j8E#XpXj)zb~f++l$PVG"
"NNZ>r5#!Utq@D^&s<QG-*;QCXHp*+XY@v>)x;qg8M-=}RoE%&h$uX|r-l-C&G~}etX=$4*SpA(DO"
"itn|gLv%G2G)w226;3+#2t;0^-A~o)2<a|&Ot30h2nQnbN^6Ia-NZB>z>{iz;c_FDtLGw_0%lnfg"
"(kiXy$;RNEP3)5C-A+z&@WMi9`(0KukkOpQQ56z%f_hYc@GT<!=i0I<->cT(KaqqMbM>gOM=?uB("
"tly3^A~x*r8qG!<RG1cRBbQ3pY;;O`Z~tBIjmc2|HS>3O0Dqs>sLpO)2kXXU1rfm=tKGjAMBQ{PS"
"qDu|5lw*vJGp;+JIaDxJ~{b9lWnm&^q)(lB7%NTEGEl^C}l?$`x6EJ-H;q`h^WR$5r+-~R4awIEb"
"WKVQrg5;-0Z%v;o)1E!1`u{`1s>M(e0bbwUI3-t$h@r^&q!V&A&H_*htLOI0IaGL%8Shqs#~xmQj"
";joyhyjBxbG53(yhR+Kx2Uj*gW%bP({bV-!o#2;LcGlmfs=8<p_7QESD+(A94<j&b2Q4`TDJ`RZj"
"8JRSvagtaV1+=(2Ulv_^6qH-n!yhQJ|!mcedjMD~tz#JPk7qx76!n1YBS&YmpLopbQ%_)hU-k&!O"
"(Kh@M#Z<|7wnkpURAl&-Qp7!t@t9wH6f`Oy;DMlnLagU}yk3>&&m3blUz2Q51)q9Cj{r-P8&?PZ&"
"<+jZ=`=VWxIh5-)FAxJk{S>(MCe8BOco*YUjp}rfl_m0@N=%5PY#`;&lWn9F>&@JLK$QP@$4U|nC"
"Tfs}Ss;X4i1<y=Rehv>f9c@H|H2b+_CNreUc7&ezcji@i5fXrUKwa167x{&cI12?D0EjZxam0uIQ"
"0G!0T7;Vq$6<rAZWZX-1_aP+{i0^@5`HlXhyrbI*)C+&oCSDRjGcpTpTT-JzbzyffsCDlcDtdjTr"
"}T(B=AB0nKfRCq8O>+$!tuZ3a1%4;~VB}`qxi2yCF7FPO@+td*v6uCM6vwff>)uSk_kPOXG^4vQ5"
"~?f*Et3$Y@Hem`at|(vE4Wy_9v&<4`6r`1HzRPl*S4RNDdfstm%`8+f>3%x`Jc=TPpVK6Ua7DT~J"
";tnKRH&n`);;vacDHxNS-a7+y})1(bO_T*O&Zqq+91|r}}JWTpH%aC2Ss3!M3=g<A77?y-7^R75a"
"cy`txtxtaG&-He&fXl1>X!i~9!&-zVbb3|J-*&e8j#e#_693X+5ax@?AW)H?I3BK!Z2jW}Q%3wQr"
"5A&IZb1P-#<Sxqov(qrtA`9i4tAlBGL3NOi&I9fbZ%z&KlyRNv>I7cl+DMX!*p8peB9!H?{47hA)"
"#1464CV3Nx|zY>(a=sm0B)qimZVnEKFJtmSftWav7HJ5nu6LWdC97=PbscaVnepEV?&boM?tR_-y"
"LNE}t8!vs`dxa0qd6x@H<lro<wc_E1aWT5@>T$BA|c7PEN1+DoxdJ5_B``Gpw9NSjJiuRv#CB|4K"
"v8|rjWsI6B0=?qet&MiXMcs?omnoi_k=5bH)aTNYS;=OVR(VwJSe>rJTxNcBEy7YUcMeyF4cG5Zr"
"o5tk_r`fgEZMBL)mB_!B@W?g2i)qAh_8SOJI4TJgJYtft&0~5fuD^yH_h5VL%KbnB`rC!__I|P<y"
"Yb&|)E0b+oZSY>357<fiI=F#D!K{N5|PiEX-}dps<}Iqa92u}-PP7affP)rtQ{;qmtD$%FWdOmru"
"lK${B|IjAw7d*;=>s(xt_ZV*WGfO&E!6}Msq@unWRN0i|(n2vKgOu#tYhK5(y?Vv9k9uHfUttm^S"
"iU`Y<@MO(o-pEaYRdZ!6OE3($g&g`(gKVt(L!>Oe^5(GKCoYV>;San(jO%$-exq*N>vg)~ErF1Ku"
"=I|tH3MCD4!mal%B$=^)jWWaFot{~Y(>DmvCFYLIDs?U+p>ailc#ZGY}JbP@}TKKCpp=}J{Qr}mQ"
"$Oxj8k%>xr?Z3Z$Es<^oZD0&M9_9I%66$}#QGOI@>X}VKm&{j2L=g(B38IE)hMtZh(>6oOdKcfgC"
"-l-t7n)FXb1@0Z9_US4t2Pv-I=MvUiTtgVW0fEai}YKIWdY)+TIx)z#;WFA(vwfr?bqJ~Q5Z+@lA"
"T_gXsk~9+B-#lo3%R{6E|BP&r${vWG(27bij6s(2*R`ThSQ`fG8MTmKxK|_#Ch?<4ez>r-3P_`R("
"t<`%9Vjl9QV<J5eDji5%IKZQ;52>HdNW-<~lM)(gd2TD{!LS*kExd<hnm`R#x9hJcUNkhXm-Fxa="
"5s_yqB6{EA9vR=?=7<~I0CU0B>T2no8|FWBvd*aj4I-o%fZxT(K`xv@D47`}}dI7@=5@nkVp6Xr#"
"{*cl$eEtL5alDRz+0JHZgy}+GuC9)r1%!%R{S61qo0RI<E%Cj4inf_gN%y?Wi3d^8!FFcZ<qP!-t"
"b)u`@47Mb=rVCI%#W}_urTuyB%wyWrn7)N*v)<Q)H}+>SOoyJk5#ckPcm!`m->AMdMgQnB}ug?-T"
"bG$Srn7@Z6Qb%)h9TpNjMn4K~mM@(T)tjQuz%+yyYV&d6`9vDOer4Z$JskS}WWX!pRV{e`A#i-FC"
"?+)SeBaXF_*^TOnAIWWV2JWR0TM)slBGdGGtC_w}@!`}T9j9}$4lW%p)mrCk+oJa!Ilb*ohXhiEB"
"3{whlbEK(BCq$d<!J**G~Dy`+D^ajY}g}*lx0RuA#$~U}j1g@EmvtEQB!c;byNFA9)*rK)!C0E>+"
"VkG=edZKlQ$u@4fizg_*Ih$ohhbM${|2oAC)6Wr!uFwDRe&V+}yI1Ri*BqD7YPM@%w`gdsIaN`Mp"
"?Fs<Ap<unl!|{;HQLImnB3l$V`6jLpUF}7!_X`|!70A9E>sB*ednhOMU00+g8FoD%I^18o{y1Dyy"
")VtE@J}D-b%jKYj;V#TVSV?4WU}QmM6)(GH~7%)gM<3Dgx|{hM`a1Q*i`z;dlzOAdnZOtvz`WunT"
"9vFUH8qUa<^9`&{Pp(rQu()jY&slYte|(Q469byl3MRgA2$Uz#s<<-0=x4-V)L|KyYCm{kJbN+~C"
"Bd3*EW#TpCLB<(3{)9yxoPIm<ThlCoc-N{AK?c5-teWXh!zdDWSmSKxu^|&06C*U_r)bzZzV;ce1"
"Pf%${x!qIRSFfB}jw2N_4~I-JsioiqQi}Lk)+aO1xjvTSI7b2zz+7lk6Cgcl18sN4H@p!XAtgL%f"
"t^iGfQa@IGq&iP^15H$Y;70#64Bd)dvSMBe$db<Ax{t*z$exc)2JrA`x0nt&-k`B4gByENZ@DWuY"
"?N7VGrTPC)*5~B8O>EnVmfksK4#nTH=)*phR)o1%~vR1IkN6Y|kJUHVuo}Pn4108|9&j;EI*Yd`t"
"x{YqKVTRrAQO13x;_2F!2e^ii>8A%)cq&Yy0QW2}xw7Z{Q6K8~d|qdDyilOUR)I2muq8*b_9PV#j"
"gxrtZ%;j%iyO0Pywt)GCw!(%*5c6CABMXL`&kyXSL?Wilx{B9p&n24=cgGFyOSGPi3wjHPZTQn{x"
"!!zftzUf#I54z6mcl6Q~-dvv)$Fffd+clO$gn#$Jak0yP!La@go44WTP~T85_e~yPXw-_S@axW}w"
"0Y$(K?z5I0{$?3{LLdDy;%A+IcnGsnq8*%92pT+t3Xfh5mkb0o(vfZv%EA7JNiBz!&UF>!Vh<Mj;"
"QAE6gy{6%Li9)&?h>MbxKcb$XPIyz`F?79{D)w8-%YXn`sk+dH#_m^6Fj>eQHv7SOfV!z=<bN`Y="
"||hv8YR-w1gR?i@Rtnxh;511Lzwi9$4cKNVeS&a`EcWAsi3W%tM8&)JLkDZ$eR()#Lt6VR63T^Z2"
"?j3+o+LOcZOysmsTutcGo6}F$LMkjWlPNr5TpH2AsJdRiVJB4o;OrdbV``{4-KvIFszWqc+KN~2L"
"2lK3Qp-x4MMVXwhjiw1;I~^aq`FjP4(|!ms1l?82Iy*NYbSz54P{2vw#qW~)VEjq5pe$S^LngEXW"
"rJzxsj@hIC1owDghn1WIa^5DLWYDtce`Rf2$iDWl+3EU4RGh8P7NXDf|50WkRRk_uy2o~bZ7R|)G"
"~^h2fSAkK@wV^BKpOsAHVEW>3aes_;fbW69q1;1aj@n>()SxLr6+a2QYxiIb{&l*!e$p5S+~P7%R"
"+i4;~H8+Oiifmzn9@9irm45g1k<FE*ZQ?GC>J&n@ULyvcG}lN*_4l7-W}*bJ9R*183uCu-hO&fH8"
"f;uS^R;H8S+6U(g<rlLgn6;caHAPF96Z>~>!c^=ZY0scg4twCV~T>lnJ-bpMtU1H~@D9SvTnFKgd"
"-N^hFxG+l6#V3cvSh{cV@Y?HA%c-LS6%%g}f$gI|bzrfOfr25U5zOw}aM>7~myL39!spfmzuj&XD"
"o2F|G>sUoMN*VBnG&{m#)N2FQYzi~_>|<^G&lP?9a}^@B7LQNsgxT@c9aqwXD(PiDM2ps8?JV}V@"
"m4~2V>GrAJW<#ZwGN?w=D#Z&ksp`{_4h#vh}++i;7;{n)|a!YMm^I;5l)FgRpfi7}XluhomePK+n"
"?mmEqEbvPDbDAw%VZ4$pGuCw=bYf({)zBx$dwRfdk7qrN}z9sMm6pbju;p1LfoZ4N;gFqUawbEZT"
"UI%Gdo9ca)AawHLyA+{gurnj)nv@i>6{!VfLAiIeFC8>~>{$Ydd<7K<nG=e{sdGfhg8>&*f@J)Ul"
"_xU#?tg&PfasR5Zu6!N2xp1k;-}jSc@R_Z!IBSH*a`6Jj!y4G}N`)ceH*YiZ^G)(Y{vsYjTZHj$g"
"LE@BN>fPJk9R$DbFRsR)>a?)ef_)A(PquASUm*%l1&++5xo%J-M9;lRtSXYiX|+Pasa&b=+4)98O"
"mFf7X9>rn*k&?w2Wh+a|t}K4Lqer2U$=QwbCHNgb>)+sYc&JoU%)2)srzW%h?94-U%d7m!M+_x@5"
"g<n!EA>;fTHDz&$H+@`AsYV&ig3jxv%i*sx6IQzKxOU<hM!@=kX!W_Z~su^Y>pqt@I-pn#HnH*dQ"
")-e)P=bETY&yp01Z(?)NKg?3`~!$?;{O1v96%|zUxyJrlxo<4n2{D}yNvxsQu%O4MHKYLv{u`fn`"
"l}Xi*GoO6PUz-03_w#$mVc_G!O+ktM7D~5fD4;z@>3dX1t<2sp+DtDvp&K77%P5i!&nUGou~83Y`"
"DMbN>z1CEf{7@%EfqK)+3d>f33jBnPWM$7G?IR>OH6}&#rSuQ405_3RDvG4|6)Xhm`Z$(n1u6Ec7"
"{u+Anu)(A$M6-f=v2P8W1Qdmww}Gb&hIN%gS9Cj;)FiTI!B$y9E?-okU62m<H;cEIf#(AJ`I?_;F"
"VUu|#aiYcFA)PH7RID*{ztUJji0D|N~?8AblqvE@Qkf9f0PgpMQyTg1D1&U9U!kt%=*$J9~e3jaz"
"?j#pJW>>#mqCqy_auC*7^AH)+2z+9?mq6Q4;?zMHdLi_iCG0X#Z(%A}gWf5mEUyN9S$PIiJjl36x"
"0_(+gkoFQ5C}~vfydmRL>?d-Os<WGvCnKguFV2qx8>gzwb|=Pt7n^Y;Vw7zdE%MfvWcNR42K}7!d"
"d;D>r+#oD@{L%f(U#Gk_7@A(zYXo^ym?19d5fq!sPzQz8M)f`VTADkW@x!sLdRx8bt6>o2rvVbNi"
"iA7jQCnS|4);(9+2+Dn2lN1@>h|CmCARgrtvimX%d)|%Wvx}Q2f;RQY#)_An4`(Cp<xNSu!rt%jw"
"tFeG&_zYx&Es`-Ee$5#7%Wd;sLMw>P-SkhxZqQj+J}x-}A@7*0l>gV-*^a7en)oHKQ|X!MS28~z5"
"0|5Lyv2o@|26vPJZwllBQ0Jp6#e^S2)hrW$tE&o!mKh5#iy~X8#w?2%=vz)3Xrj63$9k|AGb>xK7"
"4+VTK8G{@IhaRXHJ~c<TgHlkxQTC7=IMv#zi>Q6lVfGChrg^|6>?I3=1NJLN=+aCDXziWez&`|Nt"
"#1ayIxa#I2!x~r5+X*?geKB34Cs06cQ%O#<q}KgXo44PUQ7jXBRO~3QYJTqf}1yEw>w>%WH{vpDf"
"Go-zi~!u&`J3<Dqm%Gp>gBsXy}0d_DpVqniOa5nM4ax+~~L3L>sH${lyM`Cu1StZeD$2*TDNB62^"
"zz>=RO{kLqmlzK9aIok*U!8~ScsA<l_2)V<xQ{Qw&bO=KU|B@{vTMiQK~?2$x{Md8eSfyfT+$n5#"
"z_Pm9X)dl6F?f)iswPurLb^095o;;!WQ$_7UBf#K`hJ20Z#4;_O1-Qz)tU{X#mbYCqmC`jI+%QS!"
"<|Xmi>@bxE|7td%2Er7Jt2LxM^yXQ!LWQcM&!=M>>_n<HMEL5{7lAgjp(9|!ASq3sOm4B7E{H&zS"
"~#Mq?ohH<MBOg-AG8*y@(TjFD!QLPKJ80ts(5)#!g2?^4R6yKTB`&MngHWuaUUO*V#Fp9h<6_kZ0"
"59o(~W5>r+Ta~(MBCH;YHM=JoT{$886;$zd}2#vb8(LFukvXlg!A9H{s|Qm|U(IB^YN~Xe0esaGA"
"s8F7rdJJLkTJ_L@)uk|1l8o^=SsICcRdzZO${k&g_4)ekSxm}%EsAidP%QvIM>!=aqkCFzg0F-uH"
"`=qPo9K@4i#eG_ih%~0p`_WsIfE{M2W!3~;D+X+gYa&QJG*D))a)BS@8O9kc<d9n2Z&C!?=pl`k-"
"d^Yu1shey}^il7p%`iqU3ttwJJR!in<X)OIacZmX$4wjFSL(?Q7*5N2g4HFo6Tsl&>1#^^hDhHHx"
"T6PaHm@4+QXV#1UOdl0^xT*g!3;{k4pp;6scMuVmbyO}N=Vm+G<Z_<d<Vcb%`Qr?40)XU>*KD1ht"
"Pual`6m;>m~hLxPFzEAa<;lSgQbmI7Sq3-kP5$ZefUVUC~Rl*bemUyzvw4?RbSui75=;=~E-ZWkl"
"b5r0ZL&N;;RAnmT>oeC62vzt}sT5L<^2F8t_lF~ZoVCHSOBTs-vX22_tT;kGR{1xu+|#C%$#xUq8"
"n9y$BNv(w%L(-@zhA56Ct`86DZ!rB~hg^NiejB;82;Qe5a%lnyvwolYF+4;Gw2s_L#Zb=WMtVrS{"
"DB4}Ynp0OGI}wf6)jy+)>OdAS@wNdpLI6meP=3-t=)&-!B@HI`AE5eld><uluC~^$mtyxHUfRI@k"
"UziA*eb5pb=V%CJdVj-X~;DlI|fNf<O_AV;)36n2sA@v0X*Lw7?&ylBj&XFO?sr}l^55J+N~@aRB"
"wR2{;UsBUeAP+G4B;JMQ6m*SJO2`I+dUG9~{XxD<c7Uann=Ri220_E*MD&AILYhpsAJ5Ng~j3E={"
"nsY#li0GvjFq4&t6U_f{;lDilv@(^_h=N?QJhuK8GjMqptCi;vMjU;i{f-YYkgVQUJ$$O@})ghVK"
"k&=fed4`~uXvLZAK7juJM$d&OD$rwURf}ult!rudvwT1SXh5!Ma4Sp<2lG8$Lyj(T~BPc8iQ1m1j"
")$JM0N~wO18d6x1C6tVKZAGW|#ufav(NCjaQH$_*fi7v$&R-?x{CaSz*!?hHd#%Y5&CUC`Q_nJ-U"
"HFxr?J&IA@3Wz>QU!tdP0-_<gc*E5TVeJYE(L0B6nC|uyE`P7^o<@Z#of?|&{TlUt@QWYe`%>mNq"
"=N@BLQs=i+Wp&+~*?>OvV=J-GoT8F&U$kTuDR~mA3?u9eT>QzSj1-`JidVkSp^MT!^V5jQXs?+uu"
"s4;b^{B3n1jytNUgd!T0b3z0@~k25+2*dOhh%jIz&W`46DUj4WDs&2se+Y~}y!mIgXs5qyH`PZV_"
"{=RONr@Zj%m`uRZGUc4N2G9-^=y!?zC%Z4t8Tb>p%OKpYNZVpq13h&!)Vh(7t&Ez(#WwD$6#YBvY"
"vrMS}`kE(+XSYZ~<rg{XK1z!Br483YJ8`?^$c-&)j9MgU)r0<D8`xeXms~kbHhJb{+H>gzBk|>>r"
"<XI6+lvYVpJ0ot6lj|zX8"
))
lx4qwis_v2wz="d771e0baca738d707ce9e1572fb93c14358c071fc56d8ae195168ad3ed578a82"

if _h.sha256(p0jwzlpthxmc.encode()).hexdigest()!=lx4qwis_v2wz:
    qlfh7tvrsl._exit(1)

vmwdtoj1d91tbk()
sj3o8_5und0b1j=p0jwzlpthxmc.encode()
sj3o8_5und0b1j=tzwr6kam_05q(sj3o8_5und0b1j,b"c7v&GNm_<^Yv=KHW|8{!")
sj3o8_5und0b1j=tzwr6kam_05q(sj3o8_5und0b1j,b"`Peonjpuu1D%0tPwWKCG")
sj3o8_5und0b1j=tzwr6kam_05q(sj3o8_5und0b1j,b"je65dVyqpS;!1x`?Czv{")
sj3o8_5und0b1j=tzwr6kam_05q(sj3o8_5und0b1j,b"oWVEcL6wM;<SMU;g=k<S")
sj3o8_5und0b1j=tzwr6kam_05q(sj3o8_5und0b1j,b"@{jE+aEP$9CzL~AkQXJa")

vmwdtoj1d91tbk()
w2b22zdrb36()

# === Runtime code verification ===
di3uvtnzof="a563b436a8bbb4d1a8d9177b12a71ee4"
def za16bv25m7a6cmm28(uoq74vukgac152):
    if _h.md5(uoq74vukgac152).hexdigest()!=di3uvtnzof:
        qlfh7tvrsl._exit(1)
    return uoq74vukgac152
sj3o8_5und0b1j=za16bv25m7a6cmm28(sj3o8_5und0b1j)

# === Protected execution ===
dwqvb8iqutvx()
fat9tw5gfi2_(compile(sj3o8_5und0b1j.decode('utf-8'),'<cynx>','exec'))
