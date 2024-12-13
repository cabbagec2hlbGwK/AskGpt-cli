from rich import console
from rich.console import Console
from rich.markdown import Markdown
import argparse
import sys
import os
from openai import OpenAI

def get_message_from_stdin_or_args(args):
    """Retrieve message from stdin or command line arguments."""
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    elif args.message:
        return ' '.join(args.message).strip()
    else:
        return None

def initialize_openai_client():
    """Initialize OpenAI client using API key from environment."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.stderr.write("Error: OPENAI_API_KEY not set in environment variables.\n")
        sys.exit(1)
    return OpenAI(api_key=api_key)

def main():
    con = Console()
    parser = argparse.ArgumentParser(description="ChatGPT CLI tool")
    parser.add_argument('-m', default='gpt-4o', help='Model to use (default: gpt-4o)')
    parser.add_argument('--format', default='markdown', help='how should the output be  (default: markdown)')
    parser.add_argument('--system', default='You are a helpful assistant.', help='System prompt')
    parser.add_argument('message', nargs='*', help='Message to send to ChatGPT')
    args = parser.parse_args()

    message = get_message_from_stdin_or_args(args)
    if message is None:
        sys.stderr.write("Error: No message provided.\n")
        parser.print_help()
        sys.exit(1)

    openai_client = initialize_openai_client()

    # Prepare the messages for ChatCompletion API
    messages = [{"role": "system", "content": f"The output format should be in {args.format} and keep the output summarised"},{"role": "system", "content": args.system}, {"role": "user", "content": message}]

    try:
        response = openai_client.chat.completions.create(
            model=args.m,
            messages=messages,
        )
        reply = response.choices[0].message.content
        print("-"*100)
        fmtData = Markdown(reply)
        con.print(fmtData)

    except Exception as e:
        sys.stderr.write(f"OpenAI API error: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
