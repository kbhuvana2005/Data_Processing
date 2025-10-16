# Install Java if not done
sudo apt update
sudo apt install openjdk-11-jdk -y
java -version

# Download Spark (3.5.1 is stable)
cd ~
wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar -xzf spark-3.5.1-bin-hadoop3.tgz
mv spark-3.5.1-bin-hadoop3 spark

#Add Spark to PATH (so you can run pyspark anywhere):
echo 'export SPARK_HOME=~/spark' >> ~/.bashrc
echo 'export PATH=$SPARK_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

#Verify installation
pyspark --version
