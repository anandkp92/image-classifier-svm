while :
do
	now=`date`
	filename_ts=`date +'%m-%d-%Y%H'`
	filename="temp"$filename_ts".txt"
	echo "$now: `vcgencmd measure_temp`" >> $filename
	sleep 5
done
