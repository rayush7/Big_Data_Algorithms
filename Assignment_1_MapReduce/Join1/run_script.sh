rm -rf output_new
rm -rf input
hadoop fs -mkdir input
hadoop fs -put join1_File* ./input
chmod +x join1_mapper.py
chmod +x join1_reducer.py
mapred streaming -input ./input -output ./output_new -mapper ./join1_mapper.py -reducer ./join1_reducer.py