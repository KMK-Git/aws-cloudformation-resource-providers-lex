# CustomResource::Lex::Intent KendraConfiguration

Provides configuration information for the AMAZON.KendraSearchIntent intent. When you use this intent, Amazon Lex searches the specified Amazon Kendra index and returns documents from the index that match the user's utterance. For more information, see AMAZON.KendraSearchIntent.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kendraindex" title="KendraIndex">KendraIndex</a>" : <i>String</i>,
    "<a href="#queryfilterstring" title="QueryFilterString">QueryFilterString</a>" : <i>String</i>,
    "<a href="#role" title="Role">Role</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#kendraindex" title="KendraIndex">KendraIndex</a>: <i>String</i>
<a href="#queryfilterstring" title="QueryFilterString">QueryFilterString</a>: <i>String</i>
<a href="#role" title="Role">Role</a>: <i>String</i>
</pre>

## Properties

#### KendraIndex

The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the AMAZON.KendraSearchIntent intent to search. The index must be in the same account and Region as the Amazon Lex bot. If the Amazon Kendra index does not exist, you get an exception when you call the PutIntent operation.

_Required_: Yes

_Type_: String

_Minimum_: <code>20</code>

_Maximum_: <code>2048</code>

_Pattern_: <code>arn:aws[a-zA-Z-]*:kendra:[a-z]+-[a-z]+-[0-9]:[0-9]{12}:index/[a-zA-Z0-9][a-zA-Z0-9_-]*</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryFilterString

A query filter that Amazon Lex sends to Amazon Kendra to filter the response from the query. The filter is in the format defined by Amazon Kendra. For more information, see Filtering queries. You can override this filter string with a new filter string at runtime.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The Amazon Resource Name (ARN) of an IAM role that has permission to search the Amazon Kendra index. The role must be in the same account and Region as the Amazon Lex bot. If the role does not exist, you get an exception when you call the PutIntent operation.

_Required_: Yes

_Type_: String

_Minimum_: <code>20</code>

_Maximum_: <code>2048</code>

_Pattern_: <code>arn:aws[a-zA-Z-]*:iam::[0-9]{12}:role/.*</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

