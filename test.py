import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

vals = [
  -0.1925331599060314,
  -0.17853781539161706,
  0.07119912903532953,
  0.53493963051862,
  0.7665134907602258,
  0.5224442745991771,
  0.15165423854077942,
  0.0257088171235062,
  0.13789311751812133,
  0.24950982834800764,
  -0.0038170541889227805,
  -0.2552486870297843,
  -0.012905839173002531,
  0.2848058187864239,
  0.08840584621331254,
  0.025939474878099472,
  0.21054902935054734,
  -0.042503098091993124,
  -0.049381894639065296,
  0.19166501125890445,
  0.18579147792829379,
  0.1791950484570019,
  0.17375320208331255,
  0.35101420452993515,
  0.28097885746198303,
  0.09288373462404168,
  0.39834367080369315,
  0.3931591722961786,
  -0.10511733347314953,
  -0.3568009505643535,
  -0.3615013425542311,
  -0.20235953363930254,
  -0.04455721953945016,
  -0.2139356381624108,
  -0.1583668479338713,
  0.10811693046805453,
  -0.0672075529829094,
  -0.33773021230907746,
  -0.1497721877660166,
  0.2740016377692154,
  0.21253008630313097,
  0.02165786052616714,
  0.07533601329277688,
  -0.0233299646720328,
  -0.08879012043356636,
  -0.2113009619775233,
  -0.3986179816397475,
  -0.39478161229253905,
  -0.12156008987950608,
  0.31656945135224257,
  0.5261293672987981,
  0.39604929791780513,
  0.012708826514706575,
  -0.18012214898340118,
  0.1181227300643119,
  0.24573350093333501,
  0.12822778947943836,
  0.1957971609325131,
  0.08018353354414748,
  0.023573238312129652,
  0.3318401836432632,
  0.4401161160373632,
  0.2962863544048404,
  0.2966678333898539,
  0.43214542364153175,
  0.3294144186355308,
  -0.07062117068749586,
  -0.15867386838647404,
  0.11283952308413031,
  0.2594097789115202,
  0.15954545990146263,
  -0.1505507556429685,
  -0.35685004856114644,
  -0.183548455128613,
  0.006382104521661172,
  0.006633684344412194,
  0.2542591998012249,
  0.25407938592853363,
  -0.030182172522574713,
  0.18105914224556935,
  0.2212992077836024,
  -0.16588441908256385,
  -0.10289739375895321,
  0.10832914777956243,
  -0.14150139746081486,
  -0.3970365191357673,
  -0.21591986046373118,
  0.23296045127494985,
  0.4632836192241477,
  0.4806814839764779,
  0.25100577119987394,
  -0.007225551237743766,
  0.23038823465666275,
  0.44746183590828104,
  0.4157013708572296,
  0.4223541205079547,
  0.42985400109710825,
  0.21831801610366477,
  0.005811598629977183,
  0.2526518312894542,
  0.5005177246476187,
  0.5026333094988633,
  0.25491462952605537,
  -0.13655238873441597,
  -0.17678479291613447,
  -0.05314879888147155,
  0.11487452731909838,
  0.38178697722685384,
  0.3712359328090893,
  0.10707329233697116,
  0.10471188850933028,
  0.2766705500057832,
  0.19022552348535116,
  -0.09300658722738489,
  -0.3680803811893084,
  -0.488304450279291,
  -0.48898094618796867,
  -0.37082293150527545,
  -0.12077154321987696,
  0.020919634300869003,
  0.048884276356644135,
  0.18727845266513723,
  0.4044168933894313,
  0.3446374564404783,
  0.11552400741456405,
  0.11198050512994145,
  0.2506736801292222,
  0.298009583114008,
  0.04366795134021871,
  -0.17111098483285891,
  -0.17046867208756367,
  -0.34529206407470925,
  -0.25671774599084535,
  -0.010711781383410002,
  -0.13218901979477615,
  -0.2526867964099804,
  -0.38156991596138057,
  -0.2643663973332273,
  0.1175436049972806,
  0.25379873351122384,
  0.13735881266296843,
  -0.22860321138823514,
  -0.49948074847445195,
  -0.522557997132423,
  -0.2779801338365165,
  -0.0323026825792781,
  -0.28004747738067404,
  -0.5298428468412113,
  -0.5340588862317885,
  -0.45367235270548645,
  -0.1254277921270378,
  0.0768655316677663,
  0.03316407498202599,
  -0.007412615918961252,
  -0.2951222248231469,
  -0.5423808232529246,
  -0.2955714019138218,
  0.14507378235775578,
  0.09024440501466198,
  -0.35387677946722307,
  -0.5491553885971272,
  -0.5493677858746612,
  -0.5501962193036154,
  -0.5491005030983538,
  -0.547353263461875,
  -0.29892897531285156,
  0.19703030912582278,
  0.4451161440385396,
  0.4465234278089297,
  0.20042799422557522,
  -0.26974648727272954,
  -0.2862787272370235,
  0.14743635882638825,
  0.2933479771365669,
  0.022626723699638362,
  -0.2568016289754163,
  -0.3588972853659236,
  -0.3366433143732543,
  -0.14391300020347314,
  0.20723991877246467,
  0.45539695130864977,
  0.45957562341634667,
  0.16602220118520844,
  -0.014994616836423391,
  0.116659827917162,
  0.192953396928765,
  0.35532436065732603,
  0.5006900737996791,
  0.5298553015142543,
  0.40899015976343855,
  0.11298382322282974,
  0.01900345586680117,
  -0.02541870900355342,
  -0.009241731301079567,
  0.09558010689343857,
  0.016062766729127112,
  0.027293203356522952,
  0.2275327991380993,
  0.30010251749822336,
  -0.010651006188218431,
  0.07958023672879139,
  -0.2886173333402548,
  -0.4212841520608316,
  -0.30957312512286095,
  -0.13787427322304385,
  -0.02779778772887565,
  0.10084313973792042,
  0.03192509834022559,
  -0.27062564504598385,
  -0.4907590978464706,
  -0.40939284889900895,
  -0.27207067527624784,
  -0.2743072462413457,
  -0.15201741325710272,
  -0.1331482394525902,
  -0.20224397290707183,
  -0.08642691303346811,
  0.023689344693609313,
  -0.011093472061403875,
  -0.02687365900203783,
  0.10599203199502899,
  0.06937897750805874,
  -0.18880766281262548,
  -0.4049926515293184,
  -0.3274796409664313,
  -0.09805037407760261,
  -0.20332182954776165,
  -0.23108428208858756,
  -0.0826067221747899,
  -0.17122944421733344,
  -0.11365254922887526,
  0.06109259687832029,
  -0.09665816120629833,
  -0.4236972201621588,
  -0.5619902357644813,
  -0.45535001460145347,
  -0.35484389313781906,
  -0.29723490414354425,
  -0.22125025262891063,
  -0.26609458082799986,
  -0.14317294691328997,
  0.03489153525687341,
  0.03160874769652801,
  0.16096537850972564,
  0.1395250425941881,
  -0.015554031809641988,
  0.10982031443059814,
  0.11663851432409258,
  -0.23573200193895874,
  -0.492786837209927,
  -0.29856384529286994,
  0.07833311812122962,
  0.22947022640477074,
  0.23120865933476742,
  0.23324896836833328,
  0.2337084358712249,
  -0.0005680706249241441,
  -0.30397966890199746,
  -0.36236188304490063,
  -0.31214942407544444,
  -0.23987354492379726,
  -0.2233987103248295,
  -0.21690681248000251,
  -0.14743283742184227,
  0.01807891498629497,
  0.13163319242288707,
  0.12096166507453768,
  0.10855202963499375,
  0.12306201495678418,
  0.14557858811616195,
  0.15782098960821894,
  0.1489775117510364,
  0.11949105414903458,
  0.06415762378543345,
  0.012514783655096933,
  -0.01376158931889836,
  -0.013533430242641406,
  0.019870383596266753,
  0.05339226028709637,
  0.10683106482402623,
  0.1408500635782975,
  0.18907484244332998,
  0.23567133106879648,
  0.2432466204588166,
  0.2526557541173823,
  0.2550427838990859,
  0.2557515145947284,
  0.2550992614745683,
  0.25497408448071557,
  0.2572011818041797,
  0.26002435805617985,
  0.2621900244263573,
  0.2642666416235867,
  0.26525184944564717,
  0.2663423124294511,
  0.267478018383141,
  0.268473228408045,
  0.2700845959792396,
  0.2724403904942693,
  0.2752289843459408,
  0.2773846931470154,
  0.24484769342037663,
  0.2106771123618169,
  0.13622234598718183,
  0.04392389510944977,
  0.0006553318560159269,
  -0.04631625850568164,
  -0.07436617594753263,
  -0.09712325195129781,
  -0.10496904702587202,
  -0.11035067633731363,
  -0.12382655723329891,
  -0.1548203861407596,
  -0.182090648922568,
  -0.2014859959691495,
  -0.21269579512704578,
  -0.22081305612497876,
  -0.23110769706130704,
  -0.2408153459221986,
  -0.2690487565958782,
  -0.26873646216227043,
  -0.13033372930982903,
  0.03655388484666158,
  0.018751788686570098,
  -0.11944992748729802,
  -0.25085597682596306,
  -0.2959678036499107,
  -0.30343063323818276,
  -0.309382709804199,
  -0.3030789796987552,
  -0.29740694127904416,
  -0.2814375859046483,
  -0.2654790486137094,
  -0.22596611331927074,
  -0.18597009414658072,
  -0.1922538058519964,
  -0.19837871535395574,
  -0.21490600976284446,
  -0.2319772256316103,
  -0.18864102598326077,
  -0.1456105414939788,
  -0.12928581080374607,
  -0.11240189045714767,
  -0.12331526347249125,
  -0.133811524091423,
  -0.13352459521440874,
  -0.1238539274782742,
  -0.10996143075561468,
  -0.09109946144902667,
  -0.07645991317279205,
  -0.0614006067268124,
  -0.0505788318655791,
  -0.0413090381743201,
  -0.03586983723256782,
  -0.026605249541096266,
  -0.014911410887592746,
  -0.004007109259504295,
  0.006846641848344073,
  0.029136250491568715,
  0.06730655262045485,
  0.1192006168844624,
  0.1732401993668783,
  0.20867312882272832,
  0.23276915486620095,
  0.2522908067117675,
  0.2804793862477165,
  0.32630302851348514,
  0.4437278524688455,
  0.5230645715650374,
  0.3795207025046595,
  -0.0006871047724691659,
  -0.23397318361515768,
  -0.2311857933519751,
  -0.22795835537176226,
  -0.22431724327695635,
  -0.22016394279374596,
  -0.21697149630159118,
  -0.21696771364171996,
  -0.21735474630021362,
  -0.2177859696258509,
  -0.2025809389891698,
  -0.13098662087712895,
  0.10179342600778074,
  0.2203378510340915,
  0.15233297920783576,
  0.20141259630376793,
  0.3047015650947712,
  0.47812941785130464,
  0.6043801739535782,
  0.6421818681585814,
  0.6774115760865964,
  0.6685519468554162,
  0.6582936917581053,
  0.6453370896325903,
  0.6322141007432457,
  0.6176858226938381,
  0.6004494981960418,
  0.5739235430351821,
  0.45202074612725496,
  0.1642851584115685,
  0.10581005129127344,
  -0.20772802598875667,
  -0.34932636132854444,
  -0.38530045654606926,
  -0.32117954345377037,
  -0.04217236304272978,
  0.10091628657049906,
  -0.052943753162303236,
  0.10667814278469817,
  0.430463511205964,
  0.2647374419598858,
  -0.2068402387639706,
  -0.197722864101259,
  0.08033482125505137,
  0.011633687581001674,
  0.012533729914222934,
  0.03147032194461645,
  -0.00010379976315219586,
  0.0932089814490143,
  0.12130936282798126,
  0.2845748854511909,
  0.2742801287287311,
  -0.10208428326741308,
  -0.12626040568932728,
  0.06303047659412256,
  -0.11940076484061678,
  -0.11632392938354451,
  0.030176251253643482,
  -0.023875514313451626,
  0.010931016201163005,
  0.04796770080696218,
  0.1306799460924546,
  0.1524090385849271,
  0.21720750274649137,
  0.2908005927774792,
  0.14946793926218413,
  -0.0321746269101727,
  -0.034760958067069,
  0.1712393480147248,
  0.22188467384315033,
  0.16997855169314938,
  0.10526423854060694,
  -0.14921724721130847,
  -0.23186777386692173,
  0.10828228730427833,
  0.2770692762211087,
  0.1434424782529855,
  0.21603965522115579,
  0.26990399622287176,
  -0.05084028452337094,
  -0.4153624968426768,
  -0.32431903893331715,
  0.11888488059750973,
  0.15605441190325287,
  -0.07812673385245823,
  0.04401100171197668,
  0.007055307656914811,
  -0.29306171899497035,
  -0.3967325835130229,
  -0.3014890984425869,
  0.039363050975931374,
  0.2882222270568059,
  0.29101541714367646,
  0.18496575563438633,
  0.08147505121945195,
  0.27216176212345256,
  0.21358523096772522,
  -0.2801959152213446,
  -0.44442897615606414,
  -0.23938118174766335,
  -0.1886619953532062,
  -0.1587505730659667,
  0.1774198190673517,
  0.4067990381363383,
  0.3766792761162744,
  0.3588394746457718,
  0.3908667096027108,
  0.3316349905430133,
  0.029997051327011248,
  -0.11713602777463532,
  0.08735899056362953,
  0.170731027952366,
  -0.004118557226477498,
  -0.055822525344463456,
  0.15940940071822046,
  0.17462127565801133,
  -0.13161132798498243,
  -0.36179585667608916,
  -0.39652857390656937,
  -0.33791853790001836,
  -0.2654435108552544,
  -0.08375713521710852,
  0.16447682530227742,
  0.07323134815825337,
  -0.03680191669545803,
  0.050816439115697845,
  -0.11520273647236053,
  -0.106143929752465,
  0.15811293709786173,
  0.10063089820664253,
  -0.10948907148411535,
  -0.24696402990624627,
  -0.21840510360522616,
  0.07380713001773265,
  0.27788637362254837,
  0.19137840418248553,
  0.16801505901823813,
  0.1503667556529531,
  0.08523449056048296,
  0.06548813908783067,
  -0.14507942834063614,
  -0.3127227720020678,
  -0.1703407004736773,
  0.18483359103123834,
  0.26821524764461396,
  0.134435163002519,
  0.15941137806177377,
  0.032209325658218387,
  -0.1384341625024226,
  -0.056990122622721004,
  -0.011956223943215993,
  -0.07883876798140477,
  0.032556236996318114,
  0.03984791529620569,
  -0.1891752769993046,
  -0.2097930820417791,
  0.004202069328662669,
  0.15000586858603754,
  0.07557261330966648,
  -0.15964745325321972,
  -0.2884143078812351,
  -0.10352190275924039,
  0.0044289577316534295,
  -0.031018434617176613,
  -0.03822733647884616,
  -0.11825689624423907,
  0.04640396526100449,
  0.08245571945552635,
  -0.26978142503832314,
  -0.4418809346544054,
  -0.36463564878487953,
  -0.2811439744468806,
  -0.3533338806614589,
  -0.3899900057006318,
  -0.10773806208903552,
  0.026536567321839538,
  -0.11371720150691747,
  -0.02139619757924896,
  0.15139626920357263,
  0.05158689409601555,
  -0.2297661028831112,
  -0.20526308433063262,
  0.11542196826554599,
  0.3046918045425695,
  0.3216513117534425,
  0.24175202103615484,
  0.07450696591968911,
  -0.1651695628085011,
  -0.16053326535171197,
  -0.06706743497449924,
  -0.1057508853503492,
  0.08900076913111375,
  0.050838394888091665,
  -0.1648087933754363,
  -0.1342183287425988,
  -0.08115416382695072,
  -0.06698272640781441,
  -0.2733985753620519,
  -0.4432922565766131,
  -0.4212702988600663,
  -0.21244598799708203,
  0.18385479229817325,
  0.20580572036281186,
  0.004775356232008837,
  -0.024958455186883527,
  -0.008501528271235723,
  0.04955247384662434,
  -0.13302324319306674,
  -0.17021415371534826,
  0.0946795543550428,
  0.1629957480126205,
  0.33204246390344583,
  0.5044901345632018,
  0.2578988948703023,
  0.06198886221074125,
  0.35955416897629416,
  0.3770296227032446,
  0.1500234742401497,
  0.20971512194932082,
  0.1320431733568401,
  0.16593819218260353,
  0.23657779618733937,
  0.09503961584187683,
  0.25495501698700473,
  0.6016379937650955,
  0.6554184536900772,
  0.46973468280759006,
  0.2747922212320264,
  0.07537917815726161,
  -0.016985234102831287,
  0.18862876847274854,
  -0.5449992290066625,
  -0.6671401655491243,
  -0.42226378139083676,
  -0.2999028547256529,
  -0.34244474457918084,
  -0.32986031152893874,
  -0.10737933800705204,
  0.09754874334378058,
  0.023608251122556538,
  -0.28415674985960854,
  -0.542793810541671,
  -0.6012411224358609,
  -0.40678622299158057,
  0.03393418683835678,
  0.2868329969901132,
  0.04730921627406828,
  -0.191407886405385,
  -0.1842653418424758,
  -0.1784686198946619,
  0.03892369685674066,
  0.00977540404639926,
  -0.19591041095716324,
  0.09222517080666642,
  0.19965637163701716,
  -0.06303670191365399,
  -0.0357669892586719,
  -0.010133791140800208,
  -0.3060137227314385,
  -0.22866944873967854,
  -0.04364042045012573,
  -0.1069479049890466,
  0.14620865299938762,
  0.150372042736574,
  -0.0920524508030472,
  0.16119041452344574,
  0.16575948029975374,
  -0.324445031857957,
  -0.320360101791644,
  0.17866127208638416,
  0.18452514265355635,
  -0.2606516187417084,
  -0.4605059659353074,
  -0.2536985482215815,
  -0.04565567699999004,
  -0.042769416644564115,
  0.04357648907168367,
  0.008172157718643082,
  0.051605460486318123,
  0.09489948036920631,
  -0.2718473327807702,
  -0.3303012756817256,
  -0.14163249946733866,
  -0.3243374631419228,
  -0.2601779083884591,
  -0.009413753337752157,
  -0.2541833764068347,
  -0.5006611743705333,
  -0.2522960128067482,
  -0.00343033659047616,
  -0.0355220001945314,
  0.17924328273497742,
  0.4610066437546051,
  0.24919256888838087,
  -0.03446694101208886,
  -0.07133309346063084,
  -0.034245544559586075,
  0.13803039577484133,
  0.23807432096335002,
  0.17871586423686447,
  0.017031060138807383,
  -0.1375123769504102,
  0.024038414879692868,
  0.12519674882391885,
  -0.17282751191287174,
  -0.22911238972443654,
  -0.08980418618035936,
  -0.14030428669358508,
  -0.09154476974217052,
  0.06746817332573318,
  0.251779629565576,
  0.1023207022783113,
  -0.12142118404822728,
  0.09829893849768916,
  0.24901548033216125,
  0.04387673119433961,
  -0.09941491303538147,
  0.062451133125296515,
  0.1494772970364453,
  -0.027886081954336284,
  -0.018126629892116677,
  0.10882660694913285,
  -0.06258328752259322,
  -0.26025163468760265,
  -0.34786344842072986,
  -0.44157716385213097,
  -0.4298415404086987,
  -0.34950653262469256,
  -0.14278093858676882,
  0.05000224727528599,
  -0.04162177315832197,
  -0.09666912778131063,
  0.07408757456049127,
  0.07362621763033163,
  -0.25470949962935496,
  -0.2229306897418382,
  0.23254666236698204,
  0.3175992296961092,
  0.19012323110206802,
  0.06346085278883885,
  -0.06147111594043646,
  -0.0294406992774449,
  -0.22427696536245728,
  -0.24114180692948356,
  0.18440309990726128,
  0.4004584491523641,
  0.3783642346356857,
  0.3086526929503277,
  0.2564560073283834,
  0.10523182910786698,
  -0.25238686503601077,
  -0.5218686726838031,
  -0.33074682810869127,
  -0.06233434037610286,
  -0.29124495115426274,
  -0.3805767788975713,
  -0.041972277124580556,
  0.13708731868912657,
  -0.04287989918061849,
  -0.15630106916801012,
  -0.06465397749049584,
  -0.039052402571689196,
  0.019643723584184702,
  -0.11535453380305596,
  -0.3224259554726716,
  -0.19321973491445416,
  0.06647775140383361,
  0.1271127092421095,
  0.1345499578587597,
  0.07299959900803703,
  -0.09080580646967866,
  -0.0363337713557953,
  0.054734395706802635,
  0.10621913302700477,
  0.10863739717897464,
  -0.0711313792931305,
  -0.23202982823359722,
  -0.04058623460218777,
  0.06807247176745741,
  -0.04450821856196062,
  -0.03991836959899134,
  -0.2830797083985699,
  -0.2760038203491799,
  -0.021157499586833883,
  -0.2019147430875269,
  -0.37625385864729627,
  -0.22409301910585488,
  -0.08325232149427035,
  -0.0799065937646767,
  -0.0560358133258633,
  -0.1394280430701414,
  -0.07981939204559761,
  0.2173575365393347,
  0.1877527272679963,
  -0.20268824899943422,
  -0.17498310555165686,
  0.1459897785430891,
  0.2186930165778494,
  0.1642993431788447,
  0.111507283500409,
  0.3710833905896183,
  0.38244717901180236,
  -0.10194114388146969,
  -0.08878504108047824,
  0.21689219484985078,
  0.1796187881518127,
  0.05361955045645145,
  0.11468618732120309,
  0.2418372101103084,
  0.27620323817865927,
  0.33328023981661503,
  0.14343170495518198,
  0.09308617617379505,
  0.2894153080338824,
  0.15986919922802545,
  0.03269497437836203,
  0.19102606329309174,
  0.5965016259447748,
  0.8609160663082074,
  0.628747329637473,
  0.39568542718899335,
  0.41126195036129254,
  0.19359392903132125,
  0.21639946451170253,
  0.7041756994275622,
  0.9585216918155165,
  0.7346188821100892,
  0.3832515188610371,
  0.2779686743496892,
  0.037354220821750106,
  0.18606833511672882,
  -0.5479365962304867,
  -0.7877604850387097,
  -0.5335921280079107,
  -0.22404888813078075,
  -0.4088749755619919,
  -0.4597368537165058,
  -0.2634452882914646,
  -0.5050650367085869,
  -0.5004465729358178,
  -0.24784276903936386,
  -0.2423377988476464,
  -0.2376246795411702,
  -0.23183099041613545,
  -0.04332923313630038,
  -0.10232602957968082,
  -0.2795299713641783,
  0.036954841518876125,
  0.04254627169144665,
  -0.44529431058203206,
  -0.6865406440382271,
  -0.6808075392783295,
  -0.5112802269776338,
  -0.3432229640490695,
  -0.5026347580816151,
  -0.43713369093869736,
  -0.1607633181982361,
  -0.3265575359975107,
  -0.5877482415319186,
  -0.39040133405318994,
  0.04270971236419992,
  -0.009818386167066193,
  -0.19197798043676179,
  -0.12964641974102306,
  -0.21990785046860062,
  -0.2771287128893649,
  -0.39161104090787213,
  -0.5711169929624014,
  -0.5595698440443295,
  -0.2787038097066741,
  0.16695252710176076,
  0.38373477444415005,
  0.2605184266081666,
  -0.11627830468633343,
  -0.30267912982722317,
  0.0020217699564928915,
  0.13580295033640394,
  0.02414608318415981,
  0.09744360523706506,
  -0.012735820665281367,
  -0.06409270043480736,
  0.24939011686985155,
  0.3625796044980768,
  0.2233369293687814,
  0.22816533966043945,
  0.36794616162860827,
  0.2692006228921271,
  -0.12719379358511296,
  -0.21166255131014491,
  0.06340148363625735,
  0.2132637812432752,
  0.11637801677723014,
  -0.1910338620326587,
  -0.39479329045138345,
  -0.21896426145987213,
  -0.026685917405828957,
  -0.02435976139731494,
  0.22527540995174217,
  0.22681176342506687,
  -0.0560403260061718,
  0.1566732607012586,
  0.19814012100553444,
  -0.18817800939676196,
  -0.1242707434521043,
  0.08779400719710746,
  -0.16156105662460493,
  -0.4167647929063467,
  -0.23524813189567068,
  0.21402710628384564,
  0.44451777078907195,
  0.4618641521363299,
  0.2319079269469086,
  -0.026724381257781926,
  0.21062004912311272,
  0.42732019967065593,
  0.3949816557745495,
  0.4009929876549315,
  0.4077772246677417,
  0.19535510707372525,
  -0.0180987756842651,
  0.22795547614668835,
  0.47498907251563594,
  0.47611748996240166,
  0.22726205778818342,
  -0.16543431310558307,
  -0.20674931917484568,
  -0.0841297098448136,
  0.08289475874791305,
  0.3488587635069556,
  0.3372405652991784,
  0.07191055595660206,
  0.0685304963204709,
  0.2395854435483617,
  0.15215595801581364,
  -0.13210534099417526,
  -0.40814991551582436,
  -0.5292106213152825,
  -0.5305993017030747,
  -0.4130226095560292,
  -0.16340894413892154,
  -0.022118057168272556,
  0.005487527107064259,
  0.14367511727125573,
  0.36075054924964356,
  0.30089069447625916,
  0.07173540535620485,
  0.06837910495809807,
  0.20745452760506744,
  0.2552630198701135,
  0.0013902508964532129,
  -0.2127593157626993,
  -0.2112407383768477,
  -0.38512061800344705,
  -0.29532650860894105,
  -0.0478712363520494,
  -0.167913206357572,
  -0.2868148504038959,
  -0.4139436177550221,
  -0.29470690029357516,
  0.08952475512338762,
  0.22815113132350706,
  0.1141286909521646,
  -0.24936868985356825,
  -0.5175739284754629,
  -0.5377012298830419,
  -0.28988861895239904,
  -0.04081931856784021,
  -0.2852503301459607,
  -0.5315835330470993,
  -0.5320774760199831,
  -0.4477895866504601,
  -0.11539373454991353,
  0.09111901079964085,
  0.051641570217505484,
  0.015402307621456196,
  -0.26798251491540176,
  -0.5108036267869543,
  -0.25924161851085237,
  0.18631941495166532,
  0.1362340710696059,
  -0.30327786146350655,
  -0.4937964325845922,
  -0.48913771914265564,
  -0.485091120679632,
  -0.4791315966750115,
  -0.47254965504934643,
  -0.21922267934680423,
  0.28168843482895184,
  0.5345227176859659,
  0.5404543373678053,
  0.29863639661422514,
  -0.1675198733320435,
  -0.17999995815580247,
  0.2577739998785177,
  0.40737840570788775,
  0.1398955193207023,
  -0.1365867540179957,
  -0.23597171896287622,
  -0.2112988335948292,
  -0.01645255240685757,
  0.3364736694106557,
  0.5859034209604039,
  0.5907514607849476,
  0.29720084901678245,
  0.11567327326056236,
  0.24635648381836805,
  0.32100365517028884,
  0.4810758078159654,
  0.623396961483498,
  0.6486789027401934,
  0.52302792655722,
  0.22127196424575138,
  0.12070400755499672,
  0.06873225007965249,
  0.07634867502174982,
  0.17155641749495432,
  0.0811861010329173,
  0.08039465731572691,
  0.2674288779231201,
  0.3253989086884704,
  0.35902547292873477,
  0.6555524814607561,
  0.6468519471962331,
  0.19721396965429058,
  0.0255235919950905,
  0.12872696368469522,
  0.2366248008698938,
  0.3871775272942144,
  0.3955821394059515,
  -0.01231340419962007,
  -0.15488574212223133,
  0.3737164857357448,
  0.32352356391927944,
  0.005827368399462213,
  0.143664475070377,
  0.25435756537711085,
  0.08885059960796102,
  0.24425422509606487,
  0.49545002099058777,
  0.5429331033852025,
  0.5435312037189828,
  0.5153999888479666,
  0.4314334892043509,
  0.1618393296777394,
  0.0009871881626871831,
  0.05435973033391722,
  0.05367895962445987,
  0.05162297947299235,
  0.05041702386698371,
  0.04974030823769254,
  -0.1941288385930811,
  -0.3727935345095422,
  -0.14936657469856435,
  0.1887075053547129,
  0.44671250331798623,
  0.5239177077999368,
  0.32271351232553075,
  -0.12020788749192901,
  -0.4062711559104374,
  -0.20531890101556005,
  0.038626812062196966,
  0.009369568591263547,
  0.02901227875910431,
  0.07915040675331105,
  0.25536839310435794,
  0.2469902847421867,
  -0.16019179582981874,
  -0.4169852758393756,
  -0.3456144680431135,
  -0.1585065608453663,
  -0.15624050756982216,
  -0.07847661021641834,
  0.12530235155396485,
  0.08064652691956042,
  0.1529457003939602,
  0.40254834465549494,
  0.39044143735648706,
  0.11835103334673552,
  0.04166680302251439,
  0.3124503283591056,
  0.4855971609103077,
  0.48406073041879816,
  0.47000353654768356,
  0.4449494351835547,
  0.2994830305106869,
  0.06178629484454483,
  0.10225793090612664,
  0.2447104082461981,
  0.2429519201273328,
  0.11285066088600554,
  -0.08174296747511414,
  -0.1468686251183342,
  -0.08645933418770911,
  -0.027514784483560928,
  -0.03255473557370024,
  0.12354442147542405,
  0.07819869066546202,
  -0.2871484127923803,
  -0.48728823994000103,
  -0.5265384627621981,
  -0.52738962650386,
  -0.40815707960015774,
  -0.04488471596668418,
  0.11110874397451359,
  -0.030877386872030142,
  -0.08412901753597382,
  -0.11826464184853941,
  -0.19288117684765896,
  -0.22928019585054263,
  -0.22746058389102536,
  -0.14463818437611223,
  0.18134567595228554,
  0.42108889292071766,
  0.17461797238170082,
  -0.3137132563483922,
  -0.32906047170692254,
  0.14653856119281305,
  0.19996769934119468,
  -0.17162729678352734,
  -0.3223911355786332,
  -0.11923046437556238,
  0.23577064172538958,
  0.1672750441328949,
  -0.08493200911636525,
  0.04604572687378898,
  0.18460461806302594,
  0.17315686398566565,
  0.13381453463689452,
  0.16755992535675163,
  0.2477400602609454,
  0.08804524523186937,
  -0.34300386848255693,
  -0.5770730199024684,
  -0.3147194256022975,
  0.13439660530025443,
  0.33717134218654676,
  0.3669772065809936,
  0.3947333792836115,
  0.15317395188085925,
  -0.20004352135581077,
  -0.07345463377228986,
  0.029701745067573948,
  -0.21318697267583941,
  -0.0712188810101042,
  0.20243854328885455,
  0.2259593768097222,
  0.302657057255897,
  0.3819490244233964,
  0.3827240008117167,
  0.13324030857403468,
  -0.3645972542316899,
  -0.3684018039132404,
  0.020529477766100368,
  -0.00010314177638627575,
  -0.06242695901719866,
  0.08495521758479768,
  0.035078299080853304,
  0.014275633994865412,
  0.09756948087528658,
  -0.07141750835750989,
  -0.18175355257714565,
  0.10942177976152132,
  0.19433518856040305,
  -0.04125484139023937,
  -0.05710212429554238,
  0.12610106181662598,
  0.054624956945421244,
  -0.3659707087834122,
  -0.5102742062972222,
  -0.24931648241509516,
  -0.14808777666993075,
  -0.23050851247985646,
  -0.05236430578218641,
  0.13347885055677672,
  -0.013227448676863061,
  -0.1875080154211973,
  -0.2784897240796853,
  -0.31340443055596334,
  -0.16492490737032978,
  0.14733925674501058,
  0.26218438094747615,
  0.20398555327264256,
  0.16918198070445523,
  0.09062207685582938,
  0.07645446565717756,
  0.03573673118982167,
  -0.05843778810755449,
  -0.09303857366726345,
  -0.08964622263386451,
  -0.0686238341850709,
  0.046827564096929834,
  0.11288161439883705,
  -0.12261780864773826,
  -0.1899364172078598,
  -0.053789236854750844,
  -0.12087959079444897,
  -0.01286504201589285,
  0.08162242828232087,
  -0.21467446254656594,
  -0.38752916027169826,
  -0.2832221053281275,
  -0.2439727674341487,
  -0.3351521653138849,
  -0.31824404995400335,
  -0.059774298024076085,
  0.0812781197973172,
  0.06474480048014952,
  0.14145179428191312,
  0.16890909801976176,
  0.08955428149216121,
  -0.007246212284268014,
  0.014714098478161887,
  0.17390504316248107,
  0.24406301841552233,
  0.20728748340338854,
  0.2817182701139771,
  0.3402961912970432,
  0.24675345851853253,
  0.21733023799966694,
  0.17669320838867122,
  0.08149319909928332,
  0.1282285758829782,
  0.06467546597481384,
  -0.06422874180559879,
  0.05384334963881453,
  0.2326785307092562,
  0.34946479831603583,
  0.4851846039087015,
  0.4215770508859476,
  0.044619463752086,
  -0.1696575831234427,
  -0.07663697146671462,
  0.05334519550585497,
  0.043827225675582976,
  0.15889834136657927,
  0.17061549842512436,
  0.09443840791120982,
  0.2032486647016628,
  0.306436497766086,
  0.2648073843952503,
  0.24226669875173476,
  0.3684612741587365,
  0.3252699828648405,
  0.06060138584686367,
  -0.1619659772337085,
  -0.09073256027737323,
  0.13252298375718047,
  0.02118665319626191,
  -0.012528967118406065,
  0.13010987004676047,
  0.03576548184975413,
  0.08774024851249969,
  0.25700515093317877,
  0.09389824220910287,
  -0.23837080819503959,
  -0.3817657359120762,
  -0.28009757699848425,
  -0.18443205047216182,
  -0.13153072807483096,
  -0.06011951339482623,
  -0.10940190988673414,
  0.009217997534805955,
  0.1831179000306925,
  0.1758083138461553,
  0.30127638815152347,
  0.27608602354662126,
  0.1173955565930618,
  0.23929707553398188,
  0.24278076164144596,
  -0.11278638892032818,
  -0.37290059655755664,
  -0.18160051719271597,
  0.19250900597599468,
  0.3409929728132962,
  0.34021120319390513,
  0.3398627021051829,
  0.3380630189278546,
  0.33569214075632314,
  0.09871326376056047,
  -0.20608116986675915,
  -0.2656600510644906,
  -0.21708899543935345,
  -0.14633655758016628,
  -0.1312701629528367,
  -0.1260748440958842,
  -0.05778890485946141,
  0.10663986197471498,
  0.21921253870244975,
  0.20765696055842947,
  0.1944568228708741,
  0.20826569013115115,
  0.23016620574066754,
  0.24187313115339718,
  0.2325701284942545,
  0.20269532050468186,
  0.1470397953864238,
  0.09513606045568049,
  0.06865480535175947,
  0.06872878164319063,
  0.1020236785107795,
  0.13547635641365294,
  0.18888002499743853,
  0.22289219421911893,
  0.27113259941734746,
  0.31776123274402535,
  0.3253791682319709,
  0.33483536068132735,
  0.33726770952218044,
  0.33801381168223343,
  0.3373847276814384,
  0.3372622246440969,
  0.3394651789628203,
  0.3422310538227141,
  0.3442999089770572,
  0.34623385356867853,
  0.34702418584168193,
  0.34786124919348294,
  0.3486787413666196,
  0.3492846753863629,
  0.350429509810799,
  0.35223538370074325,
  0.3543846153631076,
  0.3558055544931428,
  0.32243251202662443,
  0.2873188623065195,
  0.2118083738731639,
  0.11833605832072747,
  0.07377014992733782,
  0.025372560824014727,
  -0.0042370038139990795,
  -0.028692178242845597,
  -0.038379119651386615,
  -0.04574931955763224,
  -0.061365336885317485,
  -0.0946547602028531,
  -0.12437970321405228,
  -0.14639216478011605,
  -0.16038456657856592,
  -0.17145266206339912,
  -0.1848687872941368,
  -0.1978706466069223,
  -0.22957271259690776,
  -0.232904863195174,
  -0.09832331969594167,
  0.06456581298813824,
  0.04258781897783463,
  -0.09996689524722369,
  -0.23590226916895674,
  -0.2857184987330358,
  -0.29805906877208477,
  -0.30905997346730785,
  -0.30797338189314305,
  -0.30768347008795255,
  -0.29725734411586036,
  -0.2869986726771078,
  -0.2533371741110785,
  -0.219338479416927,
  -0.23175908423658578,
  -0.24415348183473312,
  -0.26707521246664234,
  -0.2906574738598339,
  -0.25393987936970647,
  -0.21762578019188514,
  -0.2081046866071481,
  -0.19810035876553228,
  -0.2159571960116352,
  -0.23344790230713156,
  -0.24019268425965656,
  -0.2375764307179798,
  -0.23074562471694987,
  -0.21893631114877216,
  -0.2113231677567926,
  -0.20324587536006197,
  -0.1993426398148701,
  -0.1969078630287222,
  -0.1981991252102544,
  -0.19553841183421086,
  -0.19029879999994032,
  -0.18567497529485893,
  -0.18090278501339838,
  -0.16446957097406129,
  -0.13190314301635558,
  -0.08533195400638593,
  -0.036304624883789514,
  -0.00554253917936285,
  0.014256025440509815,
  0.029886776204546578,
  0.054625418618926586,
  0.09747573727063373,
  0.21244076693787517,
  0.28986942351579925,
  0.14500873314255658,
  -0.23588381743875142,
  -0.4691803770214841,
  -0.4656856522352774,
  -0.46098812322973004,
  -0.4550678134266679,
  -0.4477784290261824,
  -0.44054378313006104,
  -0.43554098614321224,
  -0.4299199995495984,
  -0.42328049772365817,
  -0.3998868036844013,
  -0.3189290997872019,
  -0.07555258842269812,
  0.05488132866683372,
  0.00012053834747950687,
  0.063862021614549,
  0.18329549020747163,
  0.3744169994903783,
  0.5199787864409158,
  0.5787788182893305,
  0.636765838372426,
  0.6524959191306214,
  0.6687349711440194,
  0.684260268855859,
  0.7016825848036625,
  0.7198436658776017,
  0.737523261430491,
  0.7482241715812765,
  0.6659454676063049,
  0.4951870554917191,
  0.31027833668056115,
  0.12269125535119174,
  0.015046715467427592,
  0.010646342217216775,
  0.1041889190059584,
  0.4066426135244861,
  0.5790605461019367,
  0.07065689778632162
]

# read ECG data from the WAV file
# sampleRate, data = scipy.io.wavfile.read('ecg.wav')
sampleRate = 100
data = vals
times = np.arange(len(data))/sampleRate

# apply a 3-pole lowpass filter at 0.1x Nyquist frequency
b, a = scipy.signal.butter(3, 0.04)
filtered = scipy.signal.filtfilt(b, a, data)

# plot the original data next to the filtered data
print(len(data))
plt.figure(figsize=(10, 4))

plt.subplot(121)
plt.plot(times[0:300], data[0:300])
plt.title("ECG Signal with Noise")
plt.margins(0, .05)

plt.subplot(122)
plt.plot(times[0:300], filtered[0:300])
plt.title("Filtered ECG Signal")
plt.margins(0, .05)

plt.tight_layout()
plt.show()