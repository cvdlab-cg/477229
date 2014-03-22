from pyplasm import *

#COSTRUZIONE DEI PIANI

verts00 = [[0,0,0],[12,0,0],[12,12,0],[0,12,0]]
verts01 = [[0,0],[12,0],[12,12],[0,12]]
verts02 = [[-1,-1],[13,-1],[13,13],[-1,13]]
floor0 = JOIN(AA(MK)(verts00))
floor1_base = JOIN(AA(MK)(verts01))
floor1_tegole = DIFFERENCE([JOIN(AA(MK)(verts02)),floor1_base])
floor1 = STRUCT([floor1_base,floor1_tegole])

verts10 = [[1,1,3],[11,1,3],[11,11,3],[1,11,3]]
verts11 = [[1,1],[11,1],[11,11],[1,11]]
verts12 = [[0,0],[12,0],[12,12],[0,12]]
verts13 = [[1,4],[2,4],[1,8],[2,8]]
floor2 = JOIN(AA(MK)(verts10))
floor3_casetta = JOIN(AA(MK)(verts13))
floor3_base = DIFFERENCE([JOIN(AA(MK)(verts11)),floor3_casetta])
floor3_tegole = DIFFERENCE([JOIN(AA(MK)(verts12)),floor3_base,floor3_casetta])
floor3 = STRUCT([floor3_base,floor3_tegole,floor3_casetta])

verts20 = [[2,2,6],[10,2,6],[10,10,6],[2,10,6]]
verts21 = [[2,2],[10,2],[10,10],[2,10]]
verts22 = [[1,1],[11,1],[11,11],[1,11]]
verts23 = [[2,5],[3,5],[2,7],[3,7]]
verts24 = [[9,5],[10,5],[9,7],[10,7]]
verts25 = [[4,2],[8,2],[4,3],[8,3]]
verts26 = [[4,9],[8,9],[4,10],[8,10]]
floor4 = JOIN(AA(MK)(verts20))
floor5_casette_piccole = STRUCT([JOIN(AA(MK)(verts23)),JOIN(AA(MK)(verts24))])
floor5_casette_grandi = STRUCT([JOIN(AA(MK)(verts25)),JOIN(AA(MK)(verts26))])
floor5_base = DIFFERENCE([JOIN(AA(MK)(verts21)),floor5_casette_piccole,floor5_casette_grandi])
floor5_tegole = DIFFERENCE([JOIN(AA(MK)(verts22)),floor5_base,floor5_casette_piccole,floor5_casette_grandi])
floor5 = STRUCT([floor5_base,floor5_tegole,floor5_casette_piccole,floor5_casette_grandi])

verts30 = [[3,3,9],[9,3,9],[9,9,9],[3,9,9]]
verts31 = [[3,3],[9,3],[9,9],[3,9]]
verts32 = [[2,2],[10,2],[10,10],[2,10]]
floor6 = JOIN(AA(MK)(verts30))
floor7_base = JOIN(AA(MK)(verts31))
floor7_tegole = DIFFERENCE([JOIN(AA(MK)(verts32)),floor7_base])
floor7 = STRUCT([floor7_base,floor7_tegole])

verts40 = [[4,4,12],[8,4,12],[8,8,12],[4,8,12]]
verts41 = [[4,4],[8,4],[8,8],[4,8]]
verts42 = [[3,3],[9,3],[9,9],[3,9]]
floor8 = JOIN(AA(MK)(verts40))
floor9_base = JOIN(AA(MK)(verts41))
floor9_tegole = DIFFERENCE([JOIN(AA(MK)(verts42)),floor9_base])
floor9 = STRUCT([floor9_base,floor9_tegole])

two_and_half_model = STRUCT([floor0,T(3)(2)(floor1),floor2,T(3)(5)(floor3),floor4,
					T(3)(8)(floor5),floor6,T(3)(11)(floor7),floor8,T(3)(14)(floor9)])

#COSTRUZIONE DELLE PARETI

verts0S = [[0,0,0],[0,0,2],[0,12,0],[0,12,2]]
verts0N = [[12,0,0],[12,0,2],[12,12,0],[12,12,2]]
verts0E = [[0,12,0],[0,12,2],[12,12,0],[12,12,2]]
verts0W = [[0,0,0],[0,0,2],[12,0,0],[12,0,2]]

south_first = JOIN(AA(MK)(verts0S))
north_first = JOIN(AA(MK)(verts0N))
east_first = JOIN(AA(MK)(verts0E))
west_first = JOIN(AA(MK)(verts0W))

floor_first = COLOR([0.21,0.39,0.54])(STRUCT([north_first,south_first,east_first,west_first]))

verts1S = [[1,1,3],[1,1,5],[1,11,3],[1,11,5]]
verts1N = [[11,1,3],[11,1,5],[11,11,3],[11,11,5]]
verts1E = [[1,11,3],[1,11,5],[11,11,3],[11,11,5]]
verts1W = [[1,1,3],[1,1,5],[11,1,3],[11,1,5]]

south_second = JOIN(AA(MK)(verts1S))
north_second = JOIN(AA(MK)(verts1N))
east_second = JOIN(AA(MK)(verts1E))
west_second = JOIN(AA(MK)(verts1W))

floor_second = COLOR([0.21,0.39,0.54])(STRUCT([north_second,south_second,east_second,west_second]))

verts2S = [[2,2,6],[2,2,8],[2,10,6],[2,10,8]]
verts2N = [[10,2,6],[10,2,8],[10,10,6],[10,10,8]]
verts2E = [[2,10,6],[2,10,8],[10,10,6],[10,10,8]]
verts2W = [[2,2,6],[2,2,8],[10,2,6],[10,2,8]]

south_third = JOIN(AA(MK)(verts2S))
north_third = JOIN(AA(MK)(verts2N))
east_third = JOIN(AA(MK)(verts2E))
west_third = JOIN(AA(MK)(verts2W))

floor_third = COLOR([0.21,0.39,0.54])(STRUCT([north_third,south_third,east_third,west_third]))

verts3S = [[3,3,9],[3,3,11],[3,9,9],[3,9,11]]
verts3N = [[9,3,9],[9,3,11],[9,9,9],[9,9,11]]
verts3E = [[3,9,9],[3,9,11],[9,9,9],[9,9,11]]
verts3W = [[3,3,9],[3,3,11],[9,3,9],[9,3,11]]

south_fourth = JOIN(AA(MK)(verts3S))
north_fourth = JOIN(AA(MK)(verts3N))
east_fourth = JOIN(AA(MK)(verts3E))
west_fourth = JOIN(AA(MK)(verts3W))

floor_fourth = COLOR([0.21,0.39,0.54])(STRUCT([north_fourth,south_fourth,east_fourth,west_fourth]))

verts4S = [[4,4,12],[4,4,14],[4,8,12],[4,8,14]]
verts4N = [[8,4,12],[8,4,14],[8,8,12],[8,8,14]]
verts4E = [[4,8,12],[4,8,14],[8,8,12],[8,8,14]]
verts4W = [[4,4,12],[4,4,14],[8,4,12],[8,4,14]]

south_fifth = JOIN(AA(MK)(verts4S))
north_fifth = JOIN(AA(MK)(verts4N))
east_fifth = JOIN(AA(MK)(verts4E))
west_fifth = JOIN(AA(MK)(verts4W))

floor_fifth = COLOR([0.21,0.39,0.54])(STRUCT([north_fifth,south_fifth,east_fifth,west_fifth]))

#COSTRUZIONE DEI TETTI

verts0TS = [[-1,-1,2],[1,1,3],[-1,13,2],[1,11,3]]
verts0TN = [[13,-1,2],[11,1,3],[13,13,2],[11,11,3]]
verts0TE = [[-1,13,2],[1,11,3],[13,13,2],[11,11,3]]
verts0TW = [[-1,-1,2],[1,1,3],[13,-1,2],[11,1,3]]

south_first_roof = JOIN(AA(MK)(verts0TS))
north_first_roof = JOIN(AA(MK)(verts0TN))
east_first_roof = JOIN(AA(MK)(verts0TE))
west_first_roof = JOIN(AA(MK)(verts0TW))

roof_first = STRUCT([south_first_roof,north_first_roof,east_first_roof,west_first_roof])

verts1TS = [[0,0,5],[2,2,6],[0,12,5],[2,10,6]]
verts1TN = [[12,0,5],[10,2,6],[12,12,5],[10,10,6]]
verts1TE = [[0,12,5],[2,10,6],[12,12,5],[10,10,6]]
verts1TW = [[0,0,5],[2,2,6],[12,0,5],[10,2,6]]

south_second_roof = JOIN(AA(MK)(verts1TS))
north_second_roof = JOIN(AA(MK)(verts1TN))
east_second_roof = JOIN(AA(MK)(verts1TE))
west_second_roof = JOIN(AA(MK)(verts1TW))

roof_second = STRUCT([south_second_roof,north_second_roof,east_second_roof,west_second_roof])

verts2TS = [[1,1,8],[3,3,9],[1,11,8],[3,9,9]]
verts2TN = [[11,1,8],[9,3,9],[11,11,8],[9,9,9]]
verts2TE = [[1,11,8],[3,9,9],[11,11,8],[9,9,9]]
verts2TW = [[1,1,8],[3,3,9],[11,1,8],[9,3,9]]

south_third_roof = JOIN(AA(MK)(verts2TS))
north_third_roof = JOIN(AA(MK)(verts2TN))
east_third_roof = JOIN(AA(MK)(verts2TE))
west_third_roof = JOIN(AA(MK)(verts2TW))

roof_third = STRUCT([south_third_roof,north_third_roof,east_third_roof,west_third_roof])

verts3TS = [[2,2,11],[4,4,12],[2,10,11],[4,8,12]]
verts3TN = [[10,2,11],[8,4,12],[10,10,11],[8,8,12]]
verts3TE = [[2,10,11],[4,8,12],[10,10,11],[8,8,12]]
verts3TW = [[2,2,11],[4,4,12],[10,2,11],[8,4,12]]

south_fourth_roof = JOIN(AA(MK)(verts3TS))
north_fourth_roof = JOIN(AA(MK)(verts3TN))
east_fourth_roof = JOIN(AA(MK)(verts3TE))
west_fourth_roof = JOIN(AA(MK)(verts3TW))

roof_fourth = STRUCT([south_fourth_roof,north_fourth_roof,east_fourth_roof,west_fourth_roof])

verts4TS = [[3,3,14],[4,6,16],[3,9,14]]
verts4TN = [[9,3,14],[8,6,16],[9,9,14]]
verts4TE = [[3,9,14],[4,6,16],[9,9,14],[8,6,16]]
verts4TW = [[3,3,14],[4,6,16],[9,3,14],[8,6,16]]

south_fifth_roof = JOIN(AA(MK)(verts4TS))
north_fifth_roof = JOIN(AA(MK)(verts4TN))
east_fifth_roof = JOIN(AA(MK)(verts4TE))
west_fifth_roof = JOIN(AA(MK)(verts4TW))

roof_fifth = STRUCT([south_fifth_roof,north_fifth_roof,east_fifth_roof,west_fifth_roof])

mock_up_3D = STRUCT([two_and_half_model,roof_first,roof_second,roof_third,roof_fourth,roof_fifth,floor_first,floor_second,floor_third,floor_fourth,floor_fifth])

VIEW(mock_up_3D)
