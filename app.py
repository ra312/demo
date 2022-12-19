# Main page for streamlit resume
import streamlit as st
import about
import resources.ast as ast


def main():
    """Main function of App"""

    ast.write_page(about)


if __name__ == "__main__":
    main()
