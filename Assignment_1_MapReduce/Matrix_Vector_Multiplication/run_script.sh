rm -rf output_new
rm -rf input
python generate_data_mv.py
hadoop fs -mkdir input
hadoop fs -put input_matrix.txt ./input
chmod +x mapper_mv.py
chmod +x reducer_mv.py
mapred streaming -input ./input -output ./output_new -mapper ./mapper_mv.py -reducer ./reducer_mv.py