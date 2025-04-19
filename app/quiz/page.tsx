import Link from "next/link"
import Image from "next/image"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { ChevronRight, Trophy, CheckCircle2 } from "lucide-react"

export default function QuizPage() {
  const quizCategories = [
    { id: "hog-rider", name: "Hog Rider", questions: 5, completed: true },
    { id: "royal-giant", name: "Royal Giant", questions: 5, completed: false },
    { id: "golem", name: "Golem", questions: 5, completed: false },
    { id: "balloon", name: "Balloon", questions: 5, completed: false },
    { id: "goblin-barrel", name: "Goblin Barrel", questions: 5, completed: false },
    { id: "giant", name: "Giant", questions: 5, completed: false },
    { id: "pekka", name: "PEKKA", questions: 5, completed: false },
    { id: "graveyard", name: "Graveyard", questions: 5, completed: false },
    { id: "ram-rider", name: "Ram Rider", questions: 5, completed: false },
  ]

  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="bg-blue-900 text-white shadow-md">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Trophy className="h-8 w-8 text-yellow-400" />
            <h1 className="text-xl md:text-2xl font-bold">Clash Counter Academy</h1>
          </div>
          <nav className="hidden md:flex gap-6">
            <Link href="/" className="hover:text-yellow-400 font-medium">
              Home
            </Link>
            <Link href="/learn" className="hover:text-yellow-400 font-medium">
              Learn
            </Link>
            <Link href="/quiz" className="hover:text-yellow-400 font-medium">
              Quiz
            </Link>
            <Link href="/about" className="hover:text-yellow-400 font-medium">
              About
            </Link>
          </nav>
          <Button variant="outline" className="md:hidden bg-transparent border-white text-white hover:bg-blue-800">
            Menu
          </Button>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow">
        <div className="container mx-auto px-4 py-8">
          <div className="flex items-center gap-2 mb-6">
            <Link href="/" className="text-blue-600 hover:underline">
              Home
            </Link>
            <ChevronRight className="h-4 w-4" />
            <span>Quiz</span>
          </div>

          <div className="mb-8">
            <h1 className="text-3xl font-bold mb-4">Test Your Knowledge</h1>
            <p className="text-lg text-gray-700 max-w-3xl">
              Challenge yourself with these quizzes to see how well you understand countering each win condition. Each
              quiz has 5 questions about optimal counters and strategies.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {quizCategories.map((category) => (
              <Card key={category.id} className="overflow-hidden hover:shadow-lg transition-shadow">
                <div className="h-40 relative bg-gray-200">
                  <Image
                    src={`/placeholder.svg?height=160&width=320&text=${encodeURIComponent(category.name)}`}
                    alt={category.name}
                    fill
                    className="object-cover"
                  />
                  {category.completed && (
                    <div className="absolute top-2 right-2 bg-green-500 text-white rounded-full p-1">
                      <CheckCircle2 className="h-5 w-5" />
                    </div>
                  )}
                </div>
                <CardHeader className="pb-2">
                  <CardTitle>{category.name} Quiz</CardTitle>
                  <CardDescription>
                    {category.questions} questions • {category.completed ? "Completed" : "Not completed"}
                  </CardDescription>
                </CardHeader>
                <CardContent className="pb-2">
                  <p className="text-sm text-gray-600">
                    Test your knowledge about countering {category.name} with this quiz.
                  </p>
                </CardContent>
                <CardFooter>
                  <Button asChild variant="outline" className="w-full">
                    <Link href={`/quiz/${category.id}`}>{category.completed ? "Retake Quiz" : "Start Quiz"}</Link>
                  </Button>
                </CardFooter>
              </Card>
            ))}
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center gap-2 mb-4 md:mb-0">
              <Trophy className="h-6 w-6 text-yellow-400" />
              <span className="text-lg font-bold">Clash Counter Academy</span>
            </div>
            <div className="flex gap-6">
              <Link href="/" className="hover:text-yellow-400">
                Home
              </Link>
              <Link href="/learn" className="hover:text-yellow-400">
                Learn
              </Link>
              <Link href="/quiz" className="hover:text-yellow-400">
                Quiz
              </Link>
              <Link href="/about" className="hover:text-yellow-400">
                About
              </Link>
            </div>
          </div>
          <div className="mt-6 text-center md:text-left text-gray-400 text-sm">
            <p>© {new Date().getFullYear()} Clash Counter Academy. Not affiliated with Supercell.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
