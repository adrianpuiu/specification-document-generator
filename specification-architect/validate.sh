#!/bin/bash
# Specification Architect Validation Helper

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SPEC_DIR="."
VERBOSE=""
GENERATE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -p|--path)
            SPEC_DIR="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE="--verbose"
            shift
            ;;
        -g|--generate)
            GENERATE="--generate-validation"
            shift
            ;;
        -h|--help)
            echo "Usage: ./validate.sh [options]"
            echo "Options:"
            echo "  -p, --path DIR         Path to spec directory"
            echo "  -v, --verbose          Verbose output"
            echo "  -g, --generate         Generate validation.md"
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

python3 "$SCRIPT_DIR/validate_specifications.py" --path "$SPEC_DIR" $VERBOSE $GENERATE
exit $?
