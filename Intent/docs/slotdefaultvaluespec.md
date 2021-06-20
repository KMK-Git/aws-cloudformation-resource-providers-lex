# CustomResource::Lex::Intent SlotDefaultValueSpec

Contains the default values for a slot. Default values are used when Amazon Lex hasn't determined a value for a slot.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultvaluelist" title="DefaultValueList">DefaultValueList</a>" : <i>[ <a href="slotdefaultvalue.md">SlotDefaultValue</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultvaluelist" title="DefaultValueList">DefaultValueList</a>: <i>
      - <a href="slotdefaultvalue.md">SlotDefaultValue</a></i>
</pre>

## Properties

#### DefaultValueList

The default values for a slot. You can specify more than one default. For example, you can specify a default value to use from a matching context variable, a session attribute, or a fixed value. The default value chosen is selected based on the order that you specify them in the list. For example, if you specify a context variable and a fixed value in that order, Amazon Lex uses the context variable if it is available, else it uses the fixed value.

_Required_: Yes

_Type_: List of <a href="slotdefaultvalue.md">SlotDefaultValue</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

