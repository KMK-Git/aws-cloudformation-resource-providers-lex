# CustomResource::Lex::Intent CodeHook

Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#messageversion" title="MessageVersion">MessageVersion</a>" : <i>String</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#messageversion" title="MessageVersion">MessageVersion</a>: <i>String</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
</pre>

## Properties

#### MessageVersion

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see [Using Lambda Functions](https://docs.aws.amazon.com/lex/latest/dg/using-lambda.html).

_Required_: Yes

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>5</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

The Amazon Resource Name (ARN) of the Lambda function.

_Required_: Yes

_Type_: String

_Minimum_: <code>20</code>

_Maximum_: <code>2048</code>

_Pattern_: <code>arn:aws[a-zA-Z-]*[a-zA-Z-]*:lambda:[a-z]+-[a-z]+(-[a-z]+)*-[0-9]:[0-9]{12}:function:[a-zA-Z0-9-_]+(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?(:[a-zA-Z0-9-_]+)?</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

