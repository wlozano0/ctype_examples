import ctypes
import time

from ctypes import *

path = 'debug\\'

hllDll = CDLL(path + "library.dll")

f1_proto = CFUNCTYPE(POINTER(c_int), POINTER(c_int))
f1_params = (1, "a1", 0),
f1_c = f1_proto(("f1", hllDll), f1_params)

def f1_test():
    print '=' * 40
    print 'Test f1'
    a1 = (c_int*3)()
    a1[0] = 1
    a1[1] = 2
    a1[2] = 3

    print 'Before: ', a1[0], a1[1], a1[2]

    f1_c(cast(pointer(a1), POINTER(c_int)))

    print 'After: ', a1[0], a1[1], a1[2], '\n'

class struct1(Structure):
    _fields_ = [("a", c_int*3), ("b", c_int*3)]

f2_proto = CFUNCTYPE(POINTER(struct1), POINTER(struct1))
f2_params = (1, "s1", 0),
f2_c = f2_proto(("f2", hllDll), f2_params)

def f2_test():
    print '=' * 40
    print 'Test f2'
    a = (c_int*3)()
    b = (c_int*3)()

    a[0] = 1
    b[0] = 2

    s1 = struct1()
    s1.a = a
    s1.b = b

    print 'Before: ',  s1.a[0], s1.b[0]

    f2_c(pointer(s1))

    print 'After: ',  s1.a[0], s1.b[0], '\n'

f70_proto = CFUNCTYPE(c_int, c_int, POINTER(c_int), c_int, POINTER(c_int))
f70_params = (1, "a1", 0), (1, "a2", 0), (1, "a3", 0), (1, "a4", 0)
f70_c = f70_proto(("f70", hllDll), f70_params)

def convertToC(a1):
    a2 = (c_int * len(a1))()
    for i in range(0, len(a1)):
        a2[i] = a1[i]

    return a2

def f70_test():
    print '=' * 40
    print 'Test f70'
    a1 = c_int(116)
    a3 = c_int(2)
    a4 = (c_int*116)()
    a2_tmp = [41,164,704,1159,869,241,220,1205,218,537,83,1404,765,1352,119,506,195,695,621,1231,27,545,1108,176,316,1143,551,439,34,212,1253,637,723,307,495,235,359,992,177,77,583,1324,388,808,821,485,1107,718,141,1285,253,943,330,426,379,242,331,1350,835,837,1112,280,1132,497,352,603,658,561,1028,189,764,1348,474,1170,508,1345,1002,202,535,811,1405,1440,230,325,536,661,828,423,1347,1053,138,146,782,152,1407,513,726,771,499,1152,709,240,517,193,280,179,1411,1005,805,1375,907,696,284,881,752,312,141,202,991,1143,170,739,835,455,1359,956,1253,213,1343,917,728,1281,177,737,1428,749,267,760,1249,212,1517,1164,1143,670,1009,606,1379,1457,433,433,940,1161,906,511,1079,1163,1056,364,616,406,674,888,1034,988,592,1016,1009,1392,954,583,605,1439,1098,1337,546,260,772,848,1542,727,1421,691,235,774,1258,1371,1454,1159,1419,656,1102,1004,904,1556,1105,1208,426,1182,483,1265,429,777,833,758,1092,1230,1237,787,478,944,802,1363,424,438,1123,533,595,990,495,482,1175,400,1376,1278,632,1489,1012,1213,1096,313,948,1432,1517,1319,1491,640,996,1331,472,1267,646,484,1536,332,1162,804,349,607,1100,496,964,1477,588,596,870,373,1274,919,829,532,561,691,1578,271,1025,1287,732,614,433,336,1011,587,1412,726,1125,1131,1468,1379,1569,396,1245,889,1011,1624,1459,1220,1064,1016,534,718,626,741,749,1522,1678,1659,1649,1043,675,592,564,654,1262,835,609,1004,924,1368,709,1373,887,1475,910,1250,965,1474,1107,969,1517,1584,341,862,476,600,517,992,807,1031,454,946,882,1125,1523,723,1552,772,676,1296,492,1338,429,760,551,684,1256,1297,770,1580,437,1353,511,1605,1470,1583,835,1683,1024,867,447,1112,1671,1099,1679,973,1144,904,1314,1462,725,681,1180,1721,893,1310,888,1648,626,1647,1138,1725,863,430,1444,734,730,1194,1519,577,1254,869,1564,921,828,840,963,1713,843,534,876,1536,1277,1695,757,1663,700,1718,692,439,1461,996,988,1694,1371,1630,549,931,1583,821,807,520,447,1101,1031,1264,621,784,470,569,754,739,822,1291,1315,1753,1727,1841,626,1447,673,1704,1847,857,1034,886,689,1731,586,1469,1735,953,1717,1168,1684,1027,584,1413,931,1803,912,524,1783,601,1480,767,1871,1089,1858,1658,552,987,1032,1004,1666,1076,1602,1134,1255,707,602,1364,1322,671,1887,1154,493,879,1703,770,1893,1441,569,851,1762,1375,617,1155,1417,1086,837,640,1764,1721,1072,1579,1310,1119,1357,1710,1287,712,543,911,734,1357,1134,1158,1232,1656,876,1676,1852,1338,1176,1205,1849,860,739,1727,1242,1336,1425,619,1585,1449,1379,1419,1937,1344,627,861,920,1849,863,1175,1645,1453,681,1091,711,1929,990,1741,1071,958,1398,1243,774,1466,636,1244,1737,1304,1903,1764,788,915,615,823,613,961,891,676,1059,766,867,916,1503,1061,1754,866,1369,647,1350,749,1606,661,923,876,592,736,1789,1666,1503,964,805,915,1047,863,1413,1621,1826,1480,815,1066,943,1534,1011,1581,826,1567,1735,1418,1934,1115,1773,788,1545,679,847,1809,1952,1206,942,984,1954,1317,1019,927,961,1782,773,1550,1102,831,1493,1944,1348,931,982,778,776,642,826,1508,1519,1005,792,1257,1665,1501,2010,1778,1149,1956,982,1799,1181,1443,1851,1840,1306,1726,1711,1673,1011,2061,1590,2069,1003,980,2006,1236,2000,1590,1017,1688,1923,1573,1810,1044,1333,2077,899,1334,1519,2066,1471,951,1749,1703,1579,1136,1195,928,1867,751,1176,2074,1562,970,1962,1785,1977,1971,923,1187,716,1741,1363,2028,930,1214,813,848,788,1670,1278,1768,1455,2063,1620,919,1301,1924,1275,1797,1568,1511,1478,1998,1481,862,1035,891,2120,2126,1648,1713,893,1707,1125,1960,1167,1295,1394,1119,1107,1929,819,2062,879,1207,801,989,1471,919,914,1875,1911,922,772,1297,1162,1914,1174,960,1099,974,1111,1480,1106,988,2115,2114,802,1198,779,1457,905,2152,2069,1900,1607,1240,964,863,1394,1871,889,1139,1176,1967,858,1483,1703,966,1106,1073,1546,1114,1112,1872,1941,2053,1909,2211,2211,1092,2176,1069,1021,1354,2093,1643,1534,1690,1606,1159,885,2132,1463,846,843,1871,1104,1892,1894,1641,1863,1846,1484,1051,1660,1969,1548,1361,1665,1330,858,1912,1754,1085,1913,1368,1921,1393,1502,1828,2094,1211,2066,1871,852,2123,1624,2210,2159,1988,2192,1804,1405,1464,1115,2233,2250,1107,896,1381,1905,1366,1166,1651,2208,1095,1987,2105,1691,2023,1837,1055,1028,2149,1935,2280,1241,977,1926,2255,1086,2259,1004,1110,1277,2077,1533,1755,971,1054,1720,1644,1229,1913,2184,1884,2010,1717,2084,2198,1923,1974,1972,1458,1616,1004,949,1350,1741,2250,2078,2047,1221,2298,1988,2288,974,1231,1659,1705,1413,1531,2174,1036,2075,1794,1041,2268,1937,1646,996,1559,2239,1861,1979,1670,1563,1720,972,1170,1592,2077,2280,1497,1549,1951,1502,1793,2296,1204,1565,1868,2179,1232,1176,1517,1509,1753,1007,2203,1356,1498,1739,1123,1241,1275,1289,1218,1004,2225,1820,1139,1827,1458,1836,2054,1053,1324,1795,1202,2180,2102,2218,1132,1482,2183,1487,1464,1458,1509,1258,1984,2323,1121,2337,1827,2265,2370,1384,2191,1484,1983,1516,1938,1941,1265,2354,1069,1405,1415,1659,1451,2169,1724,2028,1328,1252,1030,1387,1813,1291,1808,1612,2035,1902,2411,1965,1406,1989,2049,1054,2325,1218,1098,2310,2071,2070,1218,1474,2039,2102,1050,1678,1299,1503,2093,1961,1601,2007,1975,1844,1195,2423,2113,2395,1502,2406,2144,2232,2077,1831,1183,1396,1147,1494,2362,1968,1833,2222,1165,1443,2188,1871,2379,2052,2322,2366,2163,2218,1607,1326,2176,1138,1827,2302,1633,1249,1446,1410,2216,2314,1192,1542,1286,1586,2282,1168,1399,1331,1136,1766,1338,1694,2195,2512,2180,2340,1362,2079,1909,2359,1897,2030,1739,1388,1317,1192,2390,1316,2038,2123,1708,1387,1606,1259,1949,1696,2441,2041,2153,2391,1941,1221,2097,2427,1716,1474,2092,1336,1400,1545,2203,1175,1999,1185,2431,2283,1751,2302,1161,1773,1396,1991,2258,1827,1311,2013,2380,1670,1281,1432,2169,2147,1216,1876,1242,1666,2329,1196,2475,1414,1711,1797,1741,2196,1698,2127,1412,1719,1764,2567,2530,2179,1736,1920,1667,1401,2396,2404,1915,2603,1785,2037,1933,2593,2328,1305,1694,1402,2279,1814,1896,2134,2333,1562,1779,2420,1546,2558,2241,2584,1266,1227,1353,2096,2587,2046,1320,1462,1701,2568,1298,2008,1434,1689,2574,1495,1862,2078,2147,2093,1993,2313,2253,1650,2154,2000,1525,2560,1582,1720,1440,1750,1578,1747,2343,2234,2581,1351,2215,1571,1313,2386,1657,1365,2059,1931,1637,2254,2673,1899,2066,2657,2149,2443,2241,1697,1471,1327,2363,2176,1975,2052,1416,2488,2611,2470,1762,1386,2141,2661,1770,1669,1785,1481,1433,1386,2166,2516,2040,2638,1986,2566,1684,2143,2019,1703,2476,1450,2628,2368,1454,1980,1612,2411,1506,2695,1717,2508,2020,2440,2716,2656,1367,1703,2004,2037,1880,2143,1408,1658,1457,2590,1633,2297,1615,2287,2540,1762,2039,1622,2720,2442,1716,2171,2326,2547,2452,1803,2266,2126,1683,1372,2553,2238,2392,1616,1499,1375,2207,1531,1363,1799,1527,2696,1525,1612,1453,1496,1576,2374,2056,2157,2300,2454,1846,2183,1597,1830,1671,1676,2632,2099,1753,2477,1949,2569,2516,2119,2486,1934,2775,2183,2711,2050,2097,1874,2727,2565,2709,2532,1726,1498,1736,1975,2175,2410,1693,2598,1512]
    a2 = convertToC(a2_tmp)

    res = f70_c(a1, cast(pointer(a2), POINTER(c_int)), a3, cast(pointer(a4), POINTER(c_int)))

    print 'Result: ', res, '\n'

f1_test()

f2_test()

f70_test()