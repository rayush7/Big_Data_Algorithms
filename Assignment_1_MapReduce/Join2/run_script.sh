python make_join2data.py y 1000 13 > join2_gennumA.txt
python make_join2data.py y 2000 17 > join2_gennumB.txt
python make_join2data.py y 3000 19 > join2_gennumC.txt
python make_join2data.py n 100  23 > join2_genchanA.txt
python make_join2data.py n 200  19 > join2_genchanB.txt
python make_join2data.py n 300 37 > join2_genchanC.txt

rm -rf output_new
rm -rf input
hadoop fs -mkdir input
hadoop fs -put join2_gen* ./input
chmod +x join2_mapper.py
chmod +x join2_reducer.py
mapred streaming -input ./input -output ./output_new -mapper ./join2_mapper.py -reducer ./join2_reducer.py