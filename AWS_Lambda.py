import json
import boto3

sns_client = boto3.client('sns')
def lambda_handler(event, context):
	topic_arn = 'seu_topico_sns_arn'
	message = "Um novo item foi inserido no banco de dados."
	sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
	return {
        'statusCode': 200,
        'body': json.dumps('Notificação enviada com sucesso!')
    }

