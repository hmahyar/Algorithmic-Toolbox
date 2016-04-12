# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = 100000
                #int(sys.stdin.readline())
                self.parent =[62982,9282,59561,98407,95855,69586,42754,72032,48929,66137,89396,79393,85919,41380,27023,913,51008,92642,71926,37004,51275,82886,21862,94516,38926,93089,71818,9762,63366,11931,84242,51586,87895,28699,78144,78578,48652,40617,53952,89842,27097,53739,9991,64944,22668,7022,17391,17984,83655,2943,43827,74274,5066,5580,69734,31298,75331,60255,74418,49697,79905,49955,4058,33458,79602,3333,89774,43673,13025,18311,29463,82466,58636,33930,42886,66645,71534,73146,23003,89434,75355,70822,13337,54080,93199,46395,45705,17367,99161,97895,57328,92194,99597,59393,40958,21862,89847,17731,2647,50039,61970,37410,46317,87185,37786,4689,51782,50182,45662,65394,62138,91446,58018,94650,81562,21567,3022,46058,65305,58030,68490,61341,56558,56715,1106,53765,1247,99528,75885,34878,80674,74970,71844,13765,54376,19233,53271,35306,31875,94837,83993,71557,27083,68582,68628,42216,42314,89215,87324,26662,66373,13975,40125,87648,93174,99400,6163,1402,96433,66119,58535,80324,92664,98637,15928,96249,94803,87903,88550,34616,94682,44304,28934,31205,39558,85315,48309,72873,73673,23478,69344,32394,52651,92922,77376,81104,24119,57859,32236,83261,75365,75124,38587,51906,18181,35854,27399,96801,47735,20795,33428,43324,14504,31889,56700,69004,45462,31563,12585,81346,73150,46279,64203,71351,2935,27146,7810,60509,69911,42371,8355,58399,27041,53961,86416,9440,53143,50091,3033,15069,94003,39226,45746,63711,26179,31386,9327,49617,84342,47901,44413,98244,68180,36537,98492,50263,56230,41287,42278,93599,63030,14942,49728,83035,17678,9469,19683,52312,10042,82498,8263,99987,81322,16911,91760,68158,9642,5682,15931,23607,19510,52993,66643,94601,91297,41265,91724,16575,41762,54231,15922,40197,43656,36367,81190,29604,8441,78513,69584,61979,98845,77573,70198,90722,42201,96401,31229,6290,1098,84655,21472,84837,80458,30402,70633,78837,61085,53637,39147,76336,86092,40273,38113,6391,33271,72758,89376,98995,215,15509,98149,76930,3562,431,97577,49179,51267,61935,5550,42754,54305,89265,61066,46827,69052,77701,80612,40164,18375,11911,38132,60991,21153,89781,74574,32790,74566,55305,84833,62126,60029,81387,70218,12444,99091,71862,51536,29955,30361,67280,69643,56879,51393,30933,82334,60640,16328,48754,33116,6653,71838,69939,99110,18464,73764,56794,22116,81361,23983,44707,60911,97542,81635,92798,85685,79692,19926,62765,68084,4832,50110,57296,91466,69715,78536,19783,24776,25282,56790,94000,7960,24221,63491,62725,23679,76105,52881,53462,72392,13314,51449,63078,53014,43684,62230,7753,76196,9929,90609,74629,33705,84913,60904,18950,49358,42006,63831,66754,54142,97640,87358,8657,27440,5494,17696,37585,95286,8608,69587,10161,12400,78617,64303,51113,47259,13350,77062,79175,15711,51388,99758,50225,29681,98152,70627,83537,31656,49046,99739,42583,47488,88876,33929,70872,23539,69889,46517,44571,21198,57198,27909,77321,4333,41947,97448,63903,47461,59106,91806,75200,14553,63697,45439,90946,8015,40482,78671,52936,22275,44925,68399,11850,96769,91326,89121,55107,96752,51668,51443,60008,77722,83316,81496,49652,17783,55032,77505,84135,82352,1423,77353,89557,1861,36000,78875,28620,95053,31908,51182,58650,22625,77000,2708,67563,27045,45770,20749,93534,58126,18447,59148,89678,65806,68085,98831,98689,33418,56219,89900,6668,21714,92029,74068,54569,592,69841,53065,71990,75797,68387,53351,85671,55186,7433,99379,27242,13428,39937,67763,32038,41184,91194,48608,13795,149,98125,35084,3427,72813,65723,7002,85238,89973,16263,21004,97137,47730,87506,6553,72579,65748,89057,18059,19764,29392,2628,73478,95733,95202,58227,30309,808,49618,11129,39187,25318,14362,46777,84196,49806,24909,6080,80110,76007,48251,73168,62239,10713,25645,94662,68885,91828,87478,94437,84913,53586,54615,42057,21849,81504,22480,75019,45510,92765,62395,37851,82243,98563,30644,80081,67449,6748,46413,5712,98996,58538,17918,14306,87047,86102,49185,87043,86160,24566,51271,84157,65447,30218,82818,17468,32341,75394,71114,65389,89102,70502,38787,3900,17300,41515,82260,30372,32921,56245,39208,30724,67565,65950,32868,69871,76975,54470,5962,90748,43626,12570,51072,51565,65903,73450,16750,66164,89407,9972,26968,17033,20315,9700,50369,37615,33186,58426,16198,29598,13830,34234,83113,30144,56119,63133,17942,95023,44096,53188,52124,84765,69387,65067,86753,53281,59708,55769,51007,34082,82764,4328,58921,47378,38256,60085,79119,2497,77602,16625,88259,75947,87973,36103,46934,19386,55629,32685,28048,75603,10125,37244,86633,7102,71715,13898,63295,38477,15242,96061,77785,54059,82343,86105,6576,81552,2153,61223,20229,93695,23025,55570,38558,81068,74743,99393,1839,53061,62864,80142,60657,90988,74793,37813,14287,32838,84407,80178,51915,50502,42127,63990,97011,52065,48332,99177,84871,11558,61840,58832,24181,80728,46347,96988,48588,10715,75409,75241,37319,43383,68338,17560,20443,82291,49152,55573,3543,78203,59966,15925,71843,67365,66467,5801,41142,32986,67632,12600,96422,4347,12153,19716,58683,42765,68880,7819,63585,43338,89446,86391,3761,63291,98593,61136,91278,78478,68953,42481,16475,38819,79404,52339,25995,17997,5546,6128,44659,12763,13876,7502,52078,71002,16535,29465,59699,89502,3347,21285,65774,29657,48337,20926,83909,49775,34850,67979,83050,7947,28916,99720,18487,47786,2756,19152,41667,91426,6335,55952,40449,12532,84955,9459,29727,8497,79070,55696,77271,8118,4258,13710,76267,96106,82620,604,30509,99366,22943,25532,20530,84283,62170,17553,55886,97215,86048,16818,19,79513,49847,97581,15722,22597,66694,45334,69806,72346,99957,78534,16753,11787,31521,1869,49783,5250,49139,35441,74889,75534,853,50036,93944,83513,85221,1016,46538,71044,24667,55073,93113,11148,38577,50864,99207,3985,6268,27292,13867,39619,81393,43695,64926,69006,48136,84548,20378,49816,4488,69088,41842,47482,3170,88462,68624,83296,41018,45739,39000,22909,95336,90061,84435,53708,62851,80446,85448,27978,85947,15929,91798,39228,64694,58697,67932,86535,23000,90219,11303,35276,65143,31205,50686,89269,15356,76997,35798,85935,24972,77694,29876,55963,45113,95742,21640,54886,5651,48751,17177,77564,69487,25404,86097,803,59146,97002,81961,95012,51404,69338,95727,54390,29122,55075,62592,57923,37890,31537,40936,89143,78131,31453,26363,65478,99624,24471,83547,28140,51459,93449,77750,91352,24171,64245,83744,19675,80901,44886,99474,32540,60636,82839,29720,75833,35608,18140,95257,44296,64822,62484,58114,70552,35566,5868,2716,15640,79371,28384,82293,82953,83146,87521,88097,56997,3417,47109,22543,45442,28687,17894,66084,24494,18050,99658,94039,47061,39679,69880,78931,83055,77566,57064,86349,82009,5332,36972,55039,22654,11425,95624,21148,1278,9642,41902,95354,74565,5125,70216,16565,53968,83730,3479,9815,19840,74740,4094,45829,83775,83861,5735,1570,46847,98855,33124,14202,89379,77254,84964,81308,20110,1254,61010,13397,33884,18291,3478,50372,71610,65986,13966,89396,99667,54001,43607,10261,91168,60403,58255,99090,58791,51429,81879,13526,66854,14909,13640,90464,65608,17333,70005,3950,42560,62561,10813,7076,76041,92411,99315,15216,70163,93488,253,18724,55371,3112,58464,23697,21870,62241,40560,6239,94777,34538,84667,84411,85442,24886,59985,45513,86436,79967,79726,28771,54280,46091,49932,8405,96234,53570,80026,82959,83365,51468,97399,96457,75365,17346,86189,45907,71042,68232,82117,79204,15941,23846,19695,18984,39564,61379,30047,36346,46972,38373,23036,74988,9277,61971,79371,57169,60488,26643,55185,66748,51314,8277,48581,41904,39779,77854,5441,16700,72328,64202,14193,84302,28185,77927,71274,27669,92313,16059,72616,69089,52704,23662,40281,1223,56432,4198,4125,77646,37123,84996,42864,57230,80207,50741,42150,19352,41530,53072,83250,33956,88446,75793,11448,73043,75857,42989,55136,40590,92124,4549,59992,75391,92249,49210,20685,93838,77409,11992,36592,58649,87409,1346,20772,89603,41677,32471,9395,74204,43569,91512,43628,48994,37066,94442,78027,86803,80021,46939,38645,81456,96883,61194,58257,39020,85405,43228,90125,71798,30783,53657,66897,91418,18159,78706,88564,500,52948,53066,88794,42064,69955,19886,74034,54243,96926,42365,2863,29091,12657,67387,87050,48476,69099,7810,64405,74732,77354,84270,58115,94869,84004,25821,25166,37248,33616,78026,48879,55720,20581,95991,20083,92999,37602,34728,46971,33660,98609,69183,63019,81749,82322,91031,58413,29280,30365,27701,6599,33288,10226,11995,4340,41896,92026,81631,29744,24339,62932,79714,37387,39510,88804,42492,80201,26576,19661,43293,84648,64615,17130,39055,90114,86368,82409,58804,1554,45719,67363,58587,18287,9483,32627,16201,33966,87065,12517,53400,77170,64431,4766,12608,70254,80604,12567,81842,90666,62386,18650,73270,55411,99206,34083,60164,95146,65070,68243,39546,74080,60418,43964,93987,22598,95598,42003,90736,48916,7871,53023,10130,76907,55503,89081,64120,48065,68996,93377,28731,51873,83008,83410,24348,10118,86505,24382,85640,3106,3403,33467,403,33631,96145,76995,4549,70109,15541,48029,89446,95783,78520,87980,28471,77142,68801,28023,54490,69530,38429,70298,76624,36899,14358,25129,90862,85740,38307,14229,87737,46585,9763,92546,50847,65054,62591,76062,73774,20836,15862,80632,45907,13734,47638,64666,19741,95387,44225,52958,99604,86174,52409,16373,27130,99300,54191,19044,91469,44931,89142,52539,34396,6310,60734,79035,89688,35806,36928,11347,61975,28479,47544,26958,12371,22305,34526,48924,12785,90126,68213,2572,55872,87173,58800,7171,96654,76171,31443,87602,28603,1767,30998,40125,93211,17670,45777,49706,43506,51175,57210,30011,21334,80556,40610,13577,97325,79536,54701,81432,68851,79092,67488,82629,83166,87373,82427,26127,27299,84307,42802,10009,95194,18037,29247,26868,65430,39449,99019,7942,57473,29636,17582,69587,92266,14980,10181,62451,23626,64339,41785,55274,84039,68859,51644,25478,85686,84587,38940,84567,40085,1362,39325,58521,38096,2186,64858,62006,99790,57613,43984,74191,73096,66719,48672,88252,85663,38722,9631,99170,4661,71436,14112,24843,60088,35194,40135,1912,13106,52732,30285,56001,13085,29037,25305,46732,2246,53564,16517,50273,86907,66828,87415,65651,40536,89566,74732,84277,49691,24712,45323,6512,1004,71592,22744,62307,96495,36639,73322,90448,50789,33265,81161,1454,66878,47724,49553,88049,50098,38559,68810,33461,41430,60918,6005,33858,52767,88823,72043,85196,24387,19804,64577,48846,7897,72370,71660,81597,7390,31016,42336,11855,18998,21577,95067,5996,67604,14491,91620,69249,67169,79095,23879,23069,89997,53771,1163,9490,93370,96406,19280,52817,94631,55636,40948,79382,21763,21004,47714,5234,50001,52376,4837,48863,37767,27356,48580,69192,14419,30026,63627,32662,62291,4127,51648,25250,69257,76132,86880,88697,76355,67155,38868,35698,72089,35789,13914,21796,46218,74215,55520,45835,79514,18125,91366,81642,5506,1211,67232,51374,74564,99183,26079,45105,73873,14545,11842,33287,23028,98437,13785,74368,15618,77072,7214,35401,19150,67866,8586,94899,3166,71819,45955,68273,75827,10027,57165,38765,62754,47879,4976,33019,40622,9618,59508,53558,82125,43307,28070,63788,32401,70287,44802,37582,22575,8,40517,21149,3383,32162,55639,28830,62785,59553,63360,11632,92407,27678,60064,84550,72651,64664,67951,91402,31397,49111,6365,81510,24546,16906,26116,605,64987,95965,80383,27481,72111,30831,12808,53450,83172,17199,45189,12916,86591,18012,64051,5998,17711,94046,93300,63603,11087,24658,2079,17014,74156,83511,19812,75744,31489,66146,84269,41393,19723,17866,39882,84192,45877,8069,97343,7679,49597,82353,30171,31883,37504,28242,15851,39984,8900,33069,55077,48354,99239,66419,18676,67682,8734,10342,6619,38483,66647,11765,55876,6078,88327,31382,17415,79337,75503,52222,98363,90551,39426,288,95400,95484,58147,12593,71001,77502,7746,40450,94487,73487,65855,26992,81517,46993,10909,43025,84341,7220,37975,10771,35554,94140,71530,41492,66854,53493,16968,64151,43294,65070,74875,2946,51041,72942,5632,7450,99862,40469,68265,87470,65337,38244,96496,79709,50280,89512,64179,77305,66553,93453,23503,15089,43954,58682,90390,61940,81624,36174,82254,88395,61499,84674,27607,97235,77405,87106,28765,49510,18484,12646,757,83224,69487,41921,87982,74895,7597,63151,79072,75788,57586,18308,23540,77237,4287,94046,42442,57357,73424,36137,66668,96933,8414,81134,91608,54109,87277,68749,46447,83867,64048,32146,39733,34069,75745,80055,49162,82941,71845,18842,11232,85539,40596,5199,92312,52550,30029,50031,30265,59439,86248,81530,68372,23584,2635,54457,23674,20885,80302,158,26266,46472,49628,39981,77510,59725,67050,22666,52396,82608,4801,2884,31583,5514,94294,40122,93000,71318,35051,23803,89339,96744,31593,82188,85669,92888,19524,80524,63780,29930,94514,17839,13626,5524,41541,89095,76880,45658,22912,76108,95873,9066,80272,92576,29476,39910,26018,88992,46933,42310,62108,41012,97224,29765,88964,85021,6693,70485,21324,67245,90757,26602,4978,1173,46467,78777,19451,97387,90225,83456,38752,11001,10269,7048,15878,78617,85913,88678,42104,81360,47808,69285,50040,75283,36987,52223,54856,22566,58039,31778,18492,72162,6709,3184,24611,33359,67455,88991,54506,75904,69807,64538,33502,81016,16440,53173,74900,752,43749,75379,14348,59211,33552,38696,61427,85227,99393,49420,4811,66070,66031,51595,7256,38094,32731,93793,3533,96107,73820,11659,99642,37727,76053,59697,52488,67468,18700,7045,95538,16527,56880,25585,23532,68546,89058,95138,83626,6812,67460,98290,63932,97739,46980,18269,49043,84705,70485,2870,36195,12726,99778,85159,57208,57901,73578,1975,54394,53388,33905,94635,88599,34838,46803,61925,25892,70619,15767,53195,37159,61663,90877,94579,73816,91568,3237,12121,3848,52444,9725,97341,75353,48852,68766,47668,70787,17385,53495,30658,16656,80220,65464,62685,90200,12853,33433,36869,8247,1033,86092,63339,32000,80787,37420,40582,85948,55217,34676,9888,69164,97437,13473,2346,37098,17787,74828,60990,26147,96704,61655,49982,80470,78872,62233,98343,18626,98841,89987,49163,42683,10330,36203,33352,28425,69494,34875,53082,77009,12188,64989,80877,71703,75064,23631,26423,46569,78483,83266,84851,28551,19941,84166,45622,47887,10865,74394,14782,25442,55933,95004,53286,67038,37561,68701,4044,7018,99346,93642,93237,73972,55936,54490,6372,84768,99162,92611,51273,85901,23825,54398,58414,39286,72083,74929,34081,63075,66798,56820,30283,24103,84572,4024,28180,51269,85747,82052,3579,82742,21625,51494,4223,31573,96111,22871,34178,85530,39721,30368,36754,97450,80396,14286,97967,82277,55363,39353,13950,91997,26726,23418,53557,18823,32992,37753,89317,24030,22511,79814,8465,73353,78127,46695,25575,34322,12002,11404,61039,68560,84071,54524,59028,38679,67739,65818,88392,47983,8822,90012,84756,16026,40185,48027,83124,68552,2722,5842,44179,54682,20701,96513,20608,81023,55713,49792,66639,71882,68475,34141,71380,45672,34317,60436,64973,15600,37393,30567,14232,600,84031,45121,76494,18026,45274,34099,58832,32485,17935,15964,67432,98261,89210,28921,61994,88242,11439,9686,69490,25188,74743,44552,2021,27665,59758,95352,34044,55075,83547,23195,9747,36254,51755,70708,16768,39434,54428,72785,99279,28625,50602,97571,97159,33694,27472,21640,64763,6887,92505,87326,58777,65352,27156,4154,81422,2101,42530,86356,1422,46454,74269,60385,97344,37046,61698,23694,72502,4854,65114,62951,81648,30055,20978,40070,10276,6075,99206,82690,8095,3142,93194,50175,83658,47983,96037,67875,93490,85367,53596,80241,28593,87113,50922,35886,48234,87291,24899,54153,64976,73791,46940,1281,25444,53005,66257,5191,54133,38448,65177,49727,27636,31647,73080,31539,51108,74784,56371,14078,45446,98601,40427,49827,43058,66934,3584,45217,96875,80783,47747,24614,84762,27783,65089,48391,96202,85289,8288,79114,11115,2062,19933,62303,80251,31120,86343,35489,23741,95711,52548,57888,61877,88731,99148,7335,22209,28885,40955,92688,75762,80045,70443,52563,92137,66625,60246,81836,12377,66902,21482,46521,71898,4170,67432,20170,75266,52923,39629,15279,26989,27316,59325,95095,26062,2048,14738,82706,18774,50632,79741,77714,39669,11999,41415,59315,80712,65393,22493,97823,66561,21253,75454,90268,62480,12822,80174,31183,71600,86013,29600,59454,58611,55903,53806,20657,93092,68894,81612,35872,74058,49384,82856,98572,7854,64781,85992,70840,80456,18617,45686,33737,22005,45317,74701,94209,75378,24323,82440,88437,58406,84054,43471,55546,45526,48511,40503,21520,76869,27383,19903,83054,38572,47035,9632,98400,20024,83235,89067,34973,73198,86085,96636,91375,19070,53192,4314 ...0,92537,23417,99085,66543,6396,77669,23206,79409,36120,85480,41923,16440,1866,52934,61055,62984,27209,78794,87016,19331,35502,33887,11485,66358,52175,42882,63332,746,51396,94822,38099,85980,47416,76842,61426,92511,85453,1451,66485,16565,22087,20260,49268,68997,84278,35207,96924,26181,673,47125,83173,94476,39198,43506,16635,21859,20773,11035,48394,84756,50674,35329,1237,87929,98277,99357,47493,34617,33289,35369,71312,50540,75985,37286,89596,56741,28797,55752,42069,44080,28569,85248,74100,27776,25269,77948,79358,32188,43154,51393,77171,98764,31458,49146,74387,20268,9970,89304,60441,67657,77558,35074,70876,91891,67072,83794,74115,44966,21357,52424,34278,3689,72897,33640,87608,32090,47397,10813,9202,61134,68148,28246,49323,64182,82118,3533,30747,95734,39653,19981,84085,23695,71286,7868,38034,29313,15994,7652,78187,42786,52818,6901,18379,84944,35797,1697,97560,81424,30240,71855,74187,88185,75288,81831,86235,3911,84672,33058,86741,93241,72951,98408,92256,11108,79878,52710,48728,13469,53928,51221,41106,26340,45885,71209,18945,48000,66883,4839,37062,97801,84689,74066,49827,58499,70680,54457,47605,56362,92491,26353,33847,56533,50231,33558,15302,75483,92417,9848,90039,48824,21606,89880,61650,24687,43750,83310,86734,93408,56194,34749,38962,76080,96523,52757,84832,56271,12555,4430,28335,28990,76322,39802,77988,62346,67469,69484,88241,83327,48244,40961,99884,19986,60414,21091,2389,62760,73597,62819,10755,5331,56044,16320,37770,55259,81845,63894,29825,32657,76076,39988,26459,68753,77828,55598,29842,42409,93849,14202,54638,60014,36515,91768,20164,90701,34891,41433,65260,92786,75529,670,36645,10425,51618,83489,57148,13337,72692,67181,20826,3869,87268,79355,43805,56766,31753,60961,22246,13289,70494,74074,8676,84317,94152,94034,33835,18919,41113,20385,61017,96826,77843,1559,25819,9022,3035,37202,30893,23936,58631,90060,64498,32772,72277,33791,14368,34692,75788,39988,16536,92616,46856,20159,25484,83426,35520,79341,37245,16315,93907,71637,56388,82837,27697,10842,91250,25444,29823,33989,33376,79123,33086,78256,63844,73117,77711,51900,12606,29055,14932,48081,67814,22799,7614,75974,30357,94167,40592,93243,3253,19020,60526,69695,7000,87265,68236,80193,63435,50087,44216,93937,72423,62343,66112,97002,74781,73696,95456,41694,48320,89077,89517,19063,50608,38490,54000,73359,99262,78045,46088,59354,92521,45239,25699,45553,52717,26345,63108,81724,11023,55415,71152,51026,77325,89598,57411,78811,88994,45841,17721,53059,6707,41211,65383,65629,41255,97515,78741,98065,31323,6751,13891,72898,35893,33140,81067,53935,27820,95505,73436,44300,41060,55235,96664,6692,87824,58535,27708,86611,59776,89284,36934,29781,7983,17898,85719,1172,45271,86960,95364,54041,18689,90246,88892,96237,59866,13733,73926,9385,10563,50274,77612,26895,37671,29723,93747,71327,93982,96045,14154,40195,64411,35322,61165,61045,34845,63037,12295,16299,70071,12599,22996,76775,17012,93706,14909,80297,7116,26163,95126,41686,61985,67795,72762,49303,44343,95511,78895,37972,5488,97998,33687,36690,66086,71731,81055,90036,74290,75520,26166,42812,51392,61687,10640,9144,25336,90539,64723,64119,83639,15470,92546,93301,57699,3818,55789,31196,40511,4029,8470,30986,80738,71893,36000,20698,2145,56539,59701,66747,25265,10782,48480,51546,22022,175,93066,87868,71525,42145,93720,50242,1164,36646,14658,42394,16269,60259,79914,1588,67452,52343,2642,89286,19218,3174,52029,52845,16998,13378,7793,78488,82758,28652,46686,96671,94499,71401,16519,11768,21788,64173,42759,53264,97470,33085,16520,97222,11092,85873,15012,15275,99012,5481,34742,528,37142,3485,19967,44453,65685,39587,7290,93249,93435,79834,64339,28588,62795,70084,93051,86806,30461,67227,47398,49027,52890,42994,28180,24243,2556,42862,19815,40160,1704,67940,12159,98539,57176,99470,70735,29431,53958,8409,80029,14067,45544,58604,16016,45657,61081,77712,74393,64605,10574,90302,74383,31286,64680,62307,78980,18716,50800,30973,26403,15418,23632,22010,51947,92022,13232,66832,5349,63831,41867,5111,59400,29950,34259,68172,64154,82796,45488,14208,30041,15351,1382,34001,74718,64205,54727,77447,17706,90117,77174,26265,68889,46765,35566,53337,47090,28659,1938,66934,74246,13569,64696,56530,12527,45213,71090,72498,44118,44852,30457,25957,46733,2859,47349,6435,75624,30230,52850,30875,32933,13703,44654,20888,96113,12752,31177,44557,62553,40374,80579,24316,36043,94643,85906,36984,97135,63675,5809,3084,36229,5997,57393,70328,90728,14871,12811,10889,74707,45258,11163,44027,49502,54989,68092,67241,28815,58350,36553,68508,65908,43259,35216,42652,16862,6391,74116,71454,39670,2482,13711,85799,58420,39289,15585,36318,91521,71569,90000,32664,58498,30456,8805,31650,32316,27085,48969,37380,73055,8497,75890,59941,11803,74117,86914,3842,51591,12372,86159,17734,6165,90152,11524,41541,21965,94948,5893,67879,77466,21295,23425,8798,7202,62678,38357,98952,97284,20452,40545,28903,9656,38086,87269,28442,220,46417,39426,91710,61816,96203,16142,81302,72381,15871,3775,40402,76803,71816,50576,62915,15402,17334,1602,58731,43817,15090,59146,54662,74894,79618,42258,80232,26984,3952,40974,50015,70406,6786,6787,43126,50522,19296,44805,42551,86000,39868,36538,35281,97575,40407,24485,92775,27160,53616,96413,83155,94415,53129,3598,4150,19262,69319,96113,40297,35348,25924,86589,72917,12357,68209,53424,91806,33240,9602,38935,35284,9843,9633,61016,40098,77139,94805,66348,22649,5149,15425,94926,77105,1280,45770,39819,60892,4716,42737,97762,56415,3438,31079,55453,97699,23598,66718,72665,43710,4666,46160,54156,79492,81536,524,50188,36785,8442,25406,17374,57784,17360,10048,22862,85501,67921,72061,21370,12814,86949,9542,3654,7196,96194,96719,14961,2868,71136,55607,34892,87005,88540,73136,69410,22066,3935,38215,21414,74979,83895,55049,99006,9304,35642,13299,97532,79359,5535,2331,46480,50124,5272,91713,74995,18036,88689,75071,28082,1842,92342,89954,66878,54202,78899,53947,34616,37097,89459,86149,97213,70801,99333,22240,87105,14109,67295,62686,81658,93035,98233,40240,38947,81694,51573,54348,3606,77797,95166,63235,2091,72232,80658,7234,99079,82243,59179,58509,31708,58422,66787,95419,22014,29886,32776,55830,75649,86799,91653,91498,43600,53764,92684,81468,25267,68628,35576,70550,74485,67339,55646,23747,72915,85345,45870,22147,82032,90320,33200,11966,61879,83655,21399,94566,856,31016,25984,36270,79845,54031,73191,40879,30404,57703,88700,3468,10043,61448,22500,52394,23114,14260,90436,82036,27557,37842,91998,29463,76292,12948,20283,1177,83590,38701,62461,41916,87133,65583,19370,31134,91272,13804,8275,31807,4632,51141,33390,95728,83297,44030,9654,9826,86120,49133,30725,70044,76656,80113,1591,88542,378,21781,81962,39052,42522,35850,16519,61513,59756,96703,67378,31559,97330,83181,1717,25778,79622,51915,53382,17704,72568,73158,87931,55563,51446,65984,38136,66877,61758,74689,73189,84795,77238,48331,56979,26561,40636,50136,16581,81445,16989,43644,36466,61881,1436,53458,63406,95912,9738,44258,63134,12036,16533,52438,82245,51171,41213,56274,61417,93726,15231,56462,45083,99245,22574,34914,80961,13783,84597,25125,4122,50192,30977,62887,26617,55816,21383,17140,20612,46610,36081,81508,15689,38379,89622,29751,81875,89684,65201,7663,14635,1806,47935,29783,38698,48958,28879,12311,38326,15017,97952,4208,29366,31126,89508,68170,7633,40638,90789,70032,74073,62200,78921,7412,38883,92383,56779,27225,51205,83667,76843,21489,32409,16831,814,5232,11497,15973,45760,14751,89283,24816,30351,86706,89060,88492,95628,70547,67706,77097,67967,3544,96655,78755,95468,44982,31223,14991,3778,45146,92476,65226,85496,54639,95366,84419,1224,10311,78549,61695,36694,85542,41751,62163,92485,78339,50523,20884,47348,51789,10714,87787,10766,14761,61329,2920,60092,3082,45946,81799,64818,18818,81068,42861,93193,52491,99865,71860,12318,61456,7730,86368,64004,87815,26934,48122,55080,32076,64573,54982,90779,67141,39191,29611,72169,71629,88156,6070,83875,79163,13322,18922,89151,5234,59847,72518,86037,20464,77336,83345,81395,11639,76435,64529,68179,7251,84819,7236,78440,68024,64529,44978,19458,71221,44534,3692,38370,3015,19231,3627,16331,90283,87392,82066,78941,82956,62637,76872,15771,41113,16165,4746,67281,41053,29213,31703,69511,66278,44174,6917,31208,92058,21400,39776,25656,98430,3504,13292,81298,17370,78727,81186,96375,89039,38236,30008,97016,23906,8230,97538,15484,90078,9355,72948,10250,36099,2646,65749,32841,43893,49520,57032,4252,27302,11936,63440,90056,39317,89462,88340,70976,66342,44335,50223,23815,6752,96948,20656,18525,12937,98689,32846,43025,6726,74853,387,82716,94982,86497,89513,91607,9720,33041,55562,40424,99241,1513,13952,34822,82640,51458,13543,98780,71858,73638,72856,41922,66970,65180,43636,49282,54493,36633,36047,83596,18463,16927,50599,47636,93872,67599,85942,46587,80820,99801,59682,73847,54756,61483,40083,98181,66532,22261,49069,52864,63158,81042,45637,38769,50999,29467,58631,30309,60053,2889,29087,77874,95338,96488,52522,11303,77899,44974,96338,68111,99762,41629,96921,23809,50857,16238,41728,40018,81461,17616,80250,55397,12742,90020,47198,9386,37205,52587,54485,80197,91556,92434,99596,20426,27238,59261,18640,35107,11647,13333,43745,3974,76405,86763,90325,35296,2035,50836,22340,83998,94939,40247,84285,65621,38828,2769,71894,93533,89560,95275,49427,13749,61330,47922,2679,97637,59463,63061,4116,6690,57661,1806,96886,29758,51894,90264,49702,38678,63551,54257,92992,16491,76378,53686,15241,41413,24091,36001,12244,27483,39374,58119,55802,26279,53139,61272,99268,88415,43720,84976,65352,55808,72224,80777,76433,50986,23197,2619,74426,91570,60545,66075,29195,5844,80370,40774,394,2188,96782,5623,37877,94148,47033,41343,40550,99163,87688,63856,71330,22607,64386,47535,12324,93179,19457,44635,83316,64231,96170,15647,69106,66677,90984,71572,64888,34128,44255,39695,33175,10910,18477,79732,16307,69674,61465,67275,25056,10127,29878,84418,89792,69711,92432,29032,6323,54022,81951,58842,49791,56333,80878,59592,34206,2462,35698,48178,14303,83660,94336,9409,51157,44561,83993,14488,61874,84494,1754,79458,39820,70547,40504,63814,74615,39524,42874,80318,84773,11686,58552,51438,76344,96678,8814,31933,25437,29796,53312,21221,23402,55282,80500,86829,93345,21342,85696,59025,17068,78484,65012,46630,84305,52059,47351,69089,54391,19576,37353,88428,73876,2181,69094,58235,63461,9030,2726,44310,34037,52613,91130,52852,14307,49101,64300,500,81479,18987,10252,78313,20714,52815,71852,5194,8487,47217,65331,73769,24790,44808,8487,79652,44936,44218,71102,9477,36107,16246,9928,7745,92563,78071,53869,7730,16140,5373,38887,55871,38610,10004,50028,64799,90327,46858,4931,52267,10079,67281,47968,44907,26663,47418,21667,24922,2018,48461,31099,89392,56123,3012,86138,9257,13048,57868,28731,16188,88749,83437,74345,62650,22689,34596,6429,39168,52125,95593,537,72197,91493,72065,79831,44139,38919,86252,3673,16082 -1,46393,1734,96887,72271,46333,42237,9266,78440,41204,3551,21426,33162,66463,34483,96995,85972,33272,39255,90575,95017,8858,25548,75487,33617,48406,63451,9861,99158,50692,30256,61257,52364,44416,32582,67325,12928,96907,28360,29522,21741,86179,71129,8945,36768,98955,57904,88857,65225,63222,69639,62288,61852,77403,5637,63294,12903,17092,17156,25898,71558,59542,25309,12862,72477,51885,652,26885,91544,11053,537,86340,85831,12666,16650,35953,48566,24495,38687,16077,40432,20144,28752,9066,51246,63023,86140,22741,94641,79929,43727,30645,10015,36639,40469,4456,95775,76242,78108,16767,77911,93962,49645,1632,85689,88965,99692,72689,53764,98009,54792,37541,83784,75556,20181,50466,43873,2986,88156,82283,89166,94474,78678,7830,47333,33973,32874,47344,45492,57446,80238,39353,14153,28704,38744,59218,97494,41485,8009,23237,63760,46783,34179,82869,4356,59904,64745,49508,76793,93427,4034,77884,33300,15204,99598,35557,61014,84279,66990,84077,63304,62429,21621,35496,82724,3225,60091,33654,82490,56175,52531,84322,38270,39412,4857,81532,28244,73561,31241,51291,87209,77547,55709,43898,84829,49858,73727,32550,73975,17436,6115,5023,17240,28630,18320,22885,54275,16010,77842,36730,21422,44575,67301,95362,81279,88446,44487,74201,61495,84540,2914,29879,77611,61971,47142,19064,31825,67941,91375,14038,89511,58077,44780,19352,11313,89367,9788,23762,5590,82485,10157,92907,97624,51148,27576,4823,74396,50139,21035,84295,61087,57728,24794,8159,42972,65536,18766,42569,27483,48170,16134,61065,69512,50186,11272,43658,68091,11406,30170,57307,99998,92733,39721,35672,31911,6393,23155,70569,72230,18389,70652,67950,96990,97272,6328,7631,82189,81198,58274,13922,94980,1795,50110,29374,52642,653,90881,53782,1518,29428,46458,29068,45222,855,39480,45357,1289,78647,48452,58461,13293,92213,73366,56187,71963,20125,56979,76193,34087,77167,92802,39231,44976,36071,94705,22851,51768,35582,33768,93283,8782,60455,39671,53731,95229,98862,80291,79743,4530,80162,58983,6074,64524,8573,42310,21469,21420,34615,30538,37204,66324,71446,44643,52,22938,44958,84410,4192,55602,67367,91766,49933,99072,66103,79787,53209,48648,88839,88155,72159,12969,43940,19240,47005,2601,1752,64655,73547,67630,35975,99886,57733,71844,23628,93347,2933,69512,55415,71522,99061,66286,19496,15888,66606,16707,23467,89237,62023,17535,12888,98184,25470,73779,40306,71094,99421,25512,59223,18690,60287,50301,52417,85563,82854,84750,21565,3219,17376,10367,37083,87569,98101,34940,37394,98893,64630,75838,98320,49764,1333,21168,74155,75011,5922,51958,94748,25142,34540,82498,86859,81470,66215,48634,54085,39379,79047,95891,90773,82235,44514,60557,17648,4208,84856,41448,16490,1440,30393,57073,27268,18570,60161,96707,83799,77020,99722,76491,99262,74724,95834,46692,8046,81791,48146,94989,74140,6542,16717,14392,69339,78751,72600,23348,26869,66158,98905,9369,98324,94870,1011,37374,39962,89254,86901,22511,17446,56978,70510,92726,9450,22863,21738,83680,27471,22048,37701,23983,94457,88962,14855,91635,86971,16261,5607,64573,56913,55637,65821,1731,17583,27491,39736,80455,51725,87819,73584,97348,93000,90668,64361,84528,55681,80063,90495,69166,53191,77443,57186,90973,35772,88063,37486,56650,4186,67574,11305,75370,74378,23974,50671,45890,83737,22325,10611,96275,81833,4035,90567,97648,10561,77407,12089,66658,33586,48706,41161,29523,41378,42815,47339,63878,73198,32430,8861,25724,86114,42196,53607,94512,77417,40222,96022,23725,74036,2015,64199,71591,63259,87521,99773,96153,79379,93980,90081,52907,85918,56458,94056,79045,8127,51347,3691,13658,66121,66158,71279,79474,2099,67411,30577,71248,80651,35378,47527,71150,25997,94672,59261,30348,69421,74052,23342,33122,17373,22811,41823,44799,20113,72463,65111,51670,78394,55521,36632,56461,42477,88669,67306,92450,84847,60780,74034,91086,29522,87952,34440,64932,39781,70288,90893,43539,57654,40115,75774,991,52297,77044,22379,66123,14041,81619,8605,86640,15708,81870,35545,82716,21350,22938,80084,59062,3007,31383,43673,4940,57457,98222,6071,11042,68147,83467,50304,96225,34301,82563,27386,94731,27787,31742,11126,21215,97485,97118,49979,45118,58129,26394,24384,68467,31262,12386,20668,20010,7288,80508,77738,75372,13765,50830,12935,21404,16566,36062,52367,70833,95794,28027,83071,81300,61972,31902,10170,55931,6456,89846,78362,94651,68714,30652,62811,48231,41506,75021,34205,29634,57967,91493,56765,31918,11167,37170,43659,84241,22377,57493,72239,88262,58425,14858,98095,52697,14803,57974,62606,56543,56855,6993,53131,36180,43451,71178,21604,90587,33188,9430,62401,35851,85357,91099,73595,52479,31346,78420,29247,52765,30299,47687,6187,51597,61387,65133,50402,45176,47042,25009,72294,82715,58030,42365,92116,10673,10076,87862,31541,97142,56438,84873,69987,67125,11686,38070,92865,87865,8524,52638,73050,4713,58693,26977,66156,42434,94856,22691,59779,96600,5682,30617,7320,22570,57136,21241,57151,4877,91430,12965,32080,16357,92335,35746,72091,90532,11829,47780,13071,59302,14344,57728,20468,175,10159,499,50848,22076,4894,95309,18521,98315,71316,75063,20779,12786,84571,68372,94629,54997,72917,53309,19013,62973,23270,438,89220,69574,90824,12653,229,83057,93619,59546,61982,15829,85796,43691,31530,89303,19349,96252,21739,7743,94760,7068,35407,12472,72061,94281,85002,78540,63482,19313,27537,58984,28790,46854,83906,93685,24439,15409,56506,57495,12224,93009,1906]
                #list(map(int, sys.stdin.readline().split()))
        
        def compute_height(self):
                keys = []
                maxHeight = 0
                for vertex in range(self.n):
                        if not vertex in keys:
                            height = 0
                            i = vertex
                            while i != -1:
                                    height += 1
                                    i = self.parent[i]
                            maxHeight = max(maxHeight, height);
                            keys.append(vertex)
                return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()