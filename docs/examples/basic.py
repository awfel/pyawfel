import json


if __name__ == "__main__":
    with open('./docs/examples/basic_workflow.json') as f:
        data = json.load(f)

    for i, node in enumerate(data.get('steps')):
        print(f"{i+1}) {node['name']}")
        if steps := node.get('steps'):
            for j, node in enumerate(steps):
                print(f"  {i+1}.{j+1}) {node.get('name')}")
