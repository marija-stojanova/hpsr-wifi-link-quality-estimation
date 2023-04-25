rename "s/.pcap.data/.csv/" */*.data
rm */*complete_data*
sed -i 's/: //g' */*.csv
# all all the column names 
sed -i 1i"time mcs nss bw rssi throughput_monitor datarate pktlost_ack nbpkt_monitor retry nbpkt_ack pktlost_seq_initial pktlost_seq_new bad_fcs" */*.csv
# uncomment this next line to remove the 5 first samples (in case they do not have converged values)
# sed -i 2,6d */*.csv
sed -i 's/ /\t/g' */*.csv
rm */*.csv.csv

