# CustomResource::Lex::SlotType EnumerationValue

Each slot type can have a set of values. Each enumeration value represents a value the slot type can take.

For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values
+ thick
+ thin
+ stuffed

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#synonyms" title="Synonyms">Synonyms</a>" : <i>[ String, ... ]</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#synonyms" title="Synonyms">Synonyms</a>: <i>
      - String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Synonyms

Additional values related to the slot type value.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the slot type.

_Required_: Yes

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>140</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

