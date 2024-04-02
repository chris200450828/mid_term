import q6_command_stuff as qcs
import pandas as pd

qcs.link_mix()
qcs.second_link_mix()
rank_list = qcs.get_rank()
title_list = qcs.get_title()
current_box_list, total_box_list = qcs.get_box()

data = zip(rank_list, title_list, current_box_list, total_box_list)

encoding = 'utf-8-sig'
df = pd.DataFrame(data, columns=['Rank', 'Title', 'This week box', 'Total box'])
try:
    df.to_csv('Taipei_movies.csv', index=False, encoding=encoding)
except PermissionError:
    print("=======================================================================================================")
    print("close the Taipei_movies.csv first before executing main.py")
"""
 放飛自我,可讀性只是浮雲
 
          .,:,,,                                        .::,,,::.
        .::::,,;;,                                  .,;;:,,....:i:
        :i,.::::,;i:.      ....,,:::::::::,....   .;i:,.  ......;i.
        :;..:::;::::i;,,:::;:,,,,,,,,,,..,.,,:::iri:. .,:irsr:,.;i.
        ;;..,::::;;;;ri,,,.                    ..,,:;s1s1ssrr;,.;r,
        :;. ,::;ii;:,     . ...................     .;iirri;;;,,;i,
        ,i. .;ri:.   ... ............................  .,,:;:,,,;i:
        :s,.;r:... ....................................... .::;::s;
        ,1r::. .............,,,.,,:,,........................,;iir;
        ,s;...........     ..::.,;:,,.          ...............,;1s
       :i,..,.              .,:,,::,.          .......... .......;1,
      ir,....:rrssr;:,       ,,.,::.     .r5S9989398G95hr;. ....,.:s,
     ;r,..,s9855513XHAG3i   .,,,,,,,.  ,S931,.,,.;s;s&BHHA8s.,..,..:r:
    :r;..rGGh,  :SAG;;G@BS:.,,,,,,,,,.r83:      hHH1sXMBHHHM3..,,,,.ir.
   ,si,.1GS,   sBMAAX&MBMB5,,,,,,:,,.:&8       3@HXHBMBHBBH#X,.,,,,,,rr
   ;1:,,SH:   .A@&&B#&8H#BS,,,,,,,,,.,5XS,     3@MHABM&59M#As..,,,,:,is,
  .rr,,,;9&1   hBHHBB&8AMGr,,,,,,,,,,,:h&&9s;   r9&BMHBHMB9:  . .,,,,;ri.
  :1:....:5&XSi;r8BMBHHA9r:,......,,,,:ii19GG88899XHHH&GSr.      ...,:rs.
  ;s.     .:sS8G8GG889hi.        ....,,:;:,.:irssrriii:,.        ...,,i1,
  ;1,         ..,....,,isssi;,        .,,.                      ....,.i1,
  ;h:               i9HHBMBBHAX9:         .                     ...,,,rs,
  ,1i..            :A#MBBBBMHB##s                             ....,,,;si.
  .r1,..        ,..;3BMBBBHBB#Bh.     ..                    ....,,,,,i1;
   :h;..       .,..;,1XBMMMMBXs,.,, .. :: ,.               ....,,,,,,ss.
    ih: ..    .;;;, ;;:s58A3i,..    ,. ,.:,,.             ...,,,,,:,s1,
    .s1,....   .,;sh,  ,iSAXs;.    ,.  ,,.i85            ...,,,,,,:i1;
     .rh: ...     rXG9XBBM#M#MHAX3hss13&&HHXr         .....,,,,,,,ih;
      .s5: .....    i598X&&A&AAAAAA&XG851r:       ........,,,,:,,sh;
      . ihr, ...  .         ..                    ..............;shs,
         ,s1i. ...  ..,,,..,,,.,,.,,.,..       ..............,ishs.
          .:s1r,......................       ..............,ishs.
          . .:shr:.  ....                 ..............,ishs.
              .,issr;,... ...........................,is1s;.
                 .,is1si;:,....................,:;ir1sr;,
                    ..:isssssrrii;::::::;;iirsssssr;:..
                         .,::iiirsssssssssrri;;:.

"""
