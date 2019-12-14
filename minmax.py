import boto3

# "region_name" here may be different depending on your default region
client = boto3.client('ssm', region_name='us-east-1')
s3 = boto3.client('s3')

response = client.get_parameters(
   Names=['UserName'],
   WithDecryption=True
)
Key_Value = "key_value.txt"
f = open("key_value.txt", "w")
f.write('%s:%s\n' %('UserName', response['Parameters'][0]['Value']))
f.close()
response = s3.upload_file(Key_Value, "testdxc", Key_Value)
