import autogen

config_list = [
    {
        'model': 'gpt-3.5-turbo-16k',
        'api_key': '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'
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved to full satisfaction. Otherwise, reply CONTINUE, or provide a reason why the task is not solved yet."""
)

task = """Write Python code to create a basic calculator, and then store it in a file"""

user_proxy.initiate_chat(
    assistant,
    message=task
)