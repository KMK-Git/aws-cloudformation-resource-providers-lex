# CustomResource::Lex::Intent OutputContext

The specification of an output context that is set when an intent is fulfilled.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#timetoliveinseconds" title="TimeToLiveInSeconds">TimeToLiveInSeconds</a>" : <i>Integer</i>,
    "<a href="#turnstolive" title="TurnsToLive">TurnsToLive</a>" : <i>Integer</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#timetoliveinseconds" title="TimeToLiveInSeconds">TimeToLiveInSeconds</a>: <i>Integer</i>
<a href="#turnstolive" title="TurnsToLive">TurnsToLive</a>: <i>Integer</i>
</pre>

## Properties

#### Name

The name of the context.

_Required_: Yes

_Type_: String

_Pattern_: <code>^([A-Za-z]_?){1,101}$</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeToLiveInSeconds

The number of seconds that the context should be active after it is first sent in a PostContent or PostText response. You can set the value between 5 and 86,400 seconds (24 hours).

_Required_: Yes

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TurnsToLive

The number of conversation turns that the context should be active. A conversation turn is one PostContent or PostText request and the corresponding response from Amazon Lex.

_Required_: Yes

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

